import importlib.util
import sys
from pathlib import Path

SCRIPT_PATH = Path("scripts/audit_api_coverage.py")
SPEC = importlib.util.spec_from_file_location("audit_api_coverage", SCRIPT_PATH)
audit_api_coverage = importlib.util.module_from_spec(SPEC)
assert SPEC is not None
assert SPEC.loader is not None
sys.modules[SPEC.name] = audit_api_coverage
SPEC.loader.exec_module(audit_api_coverage)


def test_compare_endpoints_classifies_implemented_missing_internal_and_deprecated(
    tmp_path,
):
    source_root = tmp_path / "src" / "sonarqube"
    source_root.mkdir(parents=True)
    (source_root / "sample.py").write_text(
        "\n".join(
            [
                "class Sample:",
                "    def one(self):",
                "        return self.client._get('api/foo/search')",
                "    def two(self, key):",
                "        return self.client._post(f'api/foo/{key}')",
                "    def three(self):",
                "        return self.client._get('api/foo/create')",
            ]
        )
    )
    metadata = {
        "webServices": [
            {
                "path": "api/foo",
                "actions": [
                    {"key": "search"},
                    {"key": "create", "post": True},
                    {"key": "legacy", "deprecatedSince": "10.4"},
                    {"key": "internal", "internal": True},
                ],
            }
        ]
    }

    local = audit_api_coverage.extract_local_endpoints(source_root)
    upstream = audit_api_coverage.extract_upstream_endpoints(metadata)
    rows = audit_api_coverage.compare_endpoints(local, upstream)

    assert {
        row["endpoint"]: (row["status"], row["classification"], row["method"])
        for row in rows
    } == {
        "api/foo/{...}": ("implemented", "local-only", "POST"),
        "api/foo/create": ("method-mismatch", "public", "POST"),
        "api/foo/internal": ("missing", "internal", "GET"),
        "api/foo/legacy": ("missing", "deprecated", "GET"),
        "api/foo/search": ("implemented", "public", "GET"),
    }


def test_main_can_fail_on_missing_public_endpoint(tmp_path, capsys):
    source_root = tmp_path / "src" / "sonarqube"
    source_root.mkdir(parents=True)
    (source_root / "sample.py").write_text("self.client._get('api/foo/search')")
    metadata_file = tmp_path / "webservices.json"
    metadata_file.write_text(
        '{"webServices":[{"path":"api/foo","actions":[{"key":"missing"}]}]}'
    )

    result = audit_api_coverage.main(
        [
            "--metadata-file",
            str(metadata_file),
            "--source-root",
            str(source_root),
            "--fail-on-public-missing",
        ]
    )

    assert result == 1
    assert "`api/foo/missing`" in capsys.readouterr().out
