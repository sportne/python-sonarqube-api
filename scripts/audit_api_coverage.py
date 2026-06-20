#!/usr/bin/env python3
# ruff: noqa: UP045
"""Compare local endpoint wrappers with SonarQube Web API metadata."""

from __future__ import annotations

import argparse
import ast
import base64
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional
from urllib.request import Request, urlopen


@dataclass(frozen=True)
class UpstreamEndpoint:
    endpoint: str
    method: str
    internal: bool
    deprecated_since: Optional[str]


def extract_local_endpoints(source_root: Path) -> dict[str, set[str]]:
    endpoints: dict[str, set[str]] = {}
    for path in source_root.rglob("*.py"):
        module = ast.parse(path.read_text(), filename=str(path))
        for node in ast.walk(module):
            if not isinstance(node, ast.Call) or not node.args:
                continue
            method = _method_from_ast(node.func)
            if not method:
                continue
            endpoint = _endpoint_from_ast(node.args[0])
            if endpoint and endpoint.startswith("api/"):
                endpoints.setdefault(endpoint, set()).add(method)
    return endpoints


def extract_upstream_endpoints(metadata: dict[str, Any]) -> list[UpstreamEndpoint]:
    endpoints: list[UpstreamEndpoint] = []
    for web_service in metadata.get("webServices", []):
        path = web_service.get("path", "").strip("/")
        service_internal = bool(web_service.get("internal", False))
        for action in web_service.get("actions", []):
            key = action.get("key")
            if not path or not key:
                continue
            endpoints.append(
                UpstreamEndpoint(
                    endpoint=f"{path}/{key}",
                    method="POST" if action.get("post") else "GET",
                    internal=service_internal or bool(action.get("internal", False)),
                    deprecated_since=action.get("deprecatedSince"),
                )
            )
    return sorted(endpoints, key=lambda endpoint: endpoint.endpoint)


def compare_endpoints(
    local_endpoints: dict[str, set[str]], upstream_endpoints: list[UpstreamEndpoint]
) -> list[dict[str, str]]:
    rows = []
    for upstream in upstream_endpoints:
        local_methods = local_endpoints.get(upstream.endpoint, set())
        implemented = upstream.method in local_methods
        method_mismatch = bool(local_methods) and not implemented
        classification = "public"
        if upstream.internal:
            classification = "internal"
        if upstream.deprecated_since:
            classification = "deprecated"
        if upstream.internal and upstream.deprecated_since:
            classification = "internal, deprecated"
        rows.append(
            {
                "endpoint": upstream.endpoint,
                "method": upstream.method,
                "classification": classification,
                "status": _status(implemented, method_mismatch),
                "local_methods": ", ".join(sorted(local_methods)),
                "deprecated_since": upstream.deprecated_since or "",
            }
        )
    upstream_paths = {item.endpoint for item in upstream_endpoints}
    for endpoint in sorted(set(local_endpoints) - upstream_paths):
        rows.append(
            {
                "endpoint": endpoint,
                "method": ", ".join(sorted(local_endpoints[endpoint])),
                "classification": "local-only",
                "status": "implemented",
                "local_methods": ", ".join(sorted(local_endpoints[endpoint])),
                "deprecated_since": "",
            }
        )
    return rows


def format_markdown(rows: list[dict[str, str]]) -> str:
    lines = [
        "| Status | Classification | Upstream Method | Local Method(s) | Endpoint | Deprecated Since |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            "| {status} | {classification} | {method} | {local_methods} | `{endpoint}` | {deprecated_since} |".format(
                **row
            )
        )
    return "\n".join(lines)


def load_metadata(args: argparse.Namespace) -> dict[str, Any]:
    if args.metadata_file:
        return json.loads(Path(args.metadata_file).read_text())
    if not args.host:
        raise SystemExit("Provide --host or --metadata-file")
    return fetch_metadata(args.host, token=args.token, timeout=args.timeout)


def fetch_metadata(
    host: str, token: Optional[str] = None, timeout: int = 30
) -> dict[str, Any]:
    url = f"{host.rstrip('/')}/api/webservices/list?include_internals=true"
    headers = {"Accept": "application/json"}
    if token:
        credentials = base64.b64encode(f"{token}:".encode()).decode()
        headers["Authorization"] = f"Basic {credentials}"
    request = Request(url, headers=headers)
    with urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode())


def _endpoint_from_ast(node: ast.AST) -> Optional[str]:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value.strip("/")
    if isinstance(node, ast.JoinedStr):
        parts = []
        for value in node.values:
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                parts.append(value.value)
            elif isinstance(value, ast.FormattedValue):
                parts.append("{...}")
        return "".join(parts).strip("/")
    return None


def _method_from_ast(node: ast.AST) -> Optional[str]:
    if not isinstance(node, ast.Attribute):
        return None
    return {
        "_get": "GET",
        "_post": "POST",
        "_patch": "PATCH",
        "_delete": "DELETE",
    }.get(node.attr)


def _status(implemented: bool, method_mismatch: bool) -> str:
    if implemented:
        return "implemented"
    if method_mismatch:
        return "method-mismatch"
    return "missing"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Compare local SonarQube endpoint wrappers against "
            "api/webservices/list?include_internals=true metadata."
        )
    )
    parser.add_argument(
        "--host", help="SonarQube host, for example http://localhost:9000"
    )
    parser.add_argument("--token", help="SonarQube token for metadata requests")
    parser.add_argument("--metadata-file", help="Read webservices JSON from a file")
    parser.add_argument("--source-root", default="src/sonarqube")
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument(
        "--fail-on-public-missing",
        action="store_true",
        help="Exit with status 1 when public, non-deprecated upstream endpoints are missing.",
    )
    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    metadata = load_metadata(args)
    local = extract_local_endpoints(Path(args.source_root))
    upstream = extract_upstream_endpoints(metadata)
    rows = compare_endpoints(local, upstream)
    print(format_markdown(rows))
    if args.fail_on_public_missing and any(
        row["status"] in {"missing", "method-mismatch"}
        and row["classification"] == "public"
        for row in rows
    ):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
