"""Request contracts for the public DevOps Platform settings endpoints."""

from unittest.mock import patch

import pytest

from sonarqube import SonarQube

MANAGEMENT_CASES = [
    ("count_binding", "get", "count_binding", {"almSetting": "devops"}, {}),
    (
        "create_azure",
        "post",
        "create_azure",
        {
            "key": "devops",
            "personalAccessToken": "token",
            "url": "https://dev.azure.com/org",
        },
        {},
    ),
    (
        "create_bitbucket",
        "post",
        "create_bitbucket",
        {
            "key": "devops",
            "url": "https://bitbucket.example",
            "personalAccessToken": "token",
        },
        {},
    ),
    (
        "create_bitbucketcloud",
        "post",
        "create_bitbucketcloud",
        {
            "key": "devops",
            "workspace": "workspace",
            "clientId": "client",
            "clientSecret": "secret",
        },
        {},
    ),
    (
        "create_github",
        "post",
        "create_github",
        {
            "key": "devops",
            "url": "https://api.github.com",
            "appId": "123",
            "privateKey": "private-key",
            "clientId": "client",
            "clientSecret": "secret",
        },
        {"webhookSecret": "webhook-secret"},
    ),
    (
        "create_gitlab",
        "post",
        "create_gitlab",
        {
            "key": "devops",
            "url": "https://gitlab.example",
            "personalAccessToken": "token",
        },
        {},
    ),
    ("delete_setting", "post", "delete", {"key": "devops"}, {}),
    (
        "update_azure",
        "post",
        "update_azure",
        {"key": "devops", "url": "https://dev.azure.com/org"},
        {"newKey": "renamed", "personalAccessToken": "replacement-token"},
    ),
    (
        "update_bitbucket",
        "post",
        "update_bitbucket",
        {"key": "devops", "url": "https://bitbucket.example"},
        {"newKey": "renamed", "personalAccessToken": "replacement-token"},
    ),
    (
        "update_bitbucketcloud",
        "post",
        "update_bitbucketcloud",
        {"key": "devops", "workspace": "workspace", "clientId": "client"},
        {"newKey": "renamed", "clientSecret": "replacement-secret"},
    ),
    (
        "update_github",
        "post",
        "update_github",
        {
            "key": "devops",
            "url": "https://api.github.com",
            "appId": "123",
            "clientId": "client",
        },
        {
            "newKey": "renamed",
            "privateKey": "replacement-key",
            "clientSecret": "replacement-secret",
            "webhookSecret": "replacement-webhook",
        },
    ),
    (
        "update_gitlab",
        "post",
        "update_gitlab",
        {"key": "devops", "url": "https://gitlab.example"},
        {"newKey": "renamed", "personalAccessToken": "replacement-token"},
    ),
    ("validate", "get", "validate", {"key": "devops"}, {}),
]


@pytest.mark.parametrize(
    "method,verb,endpoint,required,optional",
    MANAGEMENT_CASES,
    ids=[case[0] for case in MANAGEMENT_CASES],
)
@pytest.mark.parametrize("include_optional", [False, True])
def test_management_request_contract(
    method, verb, endpoint, required, optional, include_optional
):
    sonar = SonarQube(host="http://localhost:9000", token="test-token")
    params = {**required, **(optional if include_optional else {})}
    with patch.object(sonar.session, verb) as request:
        response = getattr(sonar.alm_settings, method)(**params)
        request.assert_called_once_with(
            f"http://localhost:9000/api/alm_settings/{endpoint}", params=params
        )
        assert response is request.return_value


@pytest.mark.parametrize(
    "method,verb,endpoint,required,optional",
    [case for case in MANAGEMENT_CASES if case[4]],
    ids=[case[0] for case in MANAGEMENT_CASES if case[4]],
)
@pytest.mark.parametrize("empty", [None, ""])
def test_omitted_optional_strings_preserve_existing_credentials(
    method, verb, endpoint, required, optional, empty
):
    sonar = SonarQube(host="http://localhost:9000", token="test-token")
    params = {**required, **dict.fromkeys(optional, empty)}
    expected = dict(required)
    if method == "update_github" and empty == "":
        expected["webhookSecret"] = ""
    with patch.object(sonar.session, verb) as request:
        getattr(sonar.alm_settings, method)(**params)
        request.assert_called_once_with(
            f"http://localhost:9000/api/alm_settings/{endpoint}", params=expected
        )


def test_github_webhook_secret_can_be_cleared_without_replacing_other_credentials():
    sonar = SonarQube(host="http://localhost:9000", token="test-token")
    with patch.object(sonar.session, "post") as request:
        sonar.alm_settings.update_github(
            key="github",
            url="https://api.github.com",
            appId="123",
            clientId="client",
            webhookSecret="",
        )
        request.assert_called_once_with(
            "http://localhost:9000/api/alm_settings/update_github",
            params={
                "key": "github",
                "url": "https://api.github.com",
                "appId": "123",
                "clientId": "client",
                "webhookSecret": "",
            },
        )
