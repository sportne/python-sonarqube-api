"""Small server compatibility checks independent of scanner provisioning."""

import os
import uuid

import pytest

from sonarqube import SonarQubeClient


@pytest.fixture
def smoke_client():
    return SonarQubeClient(
        os.environ.get("SONARQUBE_HOST", "http://localhost:9000"),
        user=os.environ.get("SONARQUBE_USER", "admin"),
        password=os.environ.get("SONARQUBE_PASSWORD", "admin"),
    )


def test_server_authentication(smoke_client):
    response = smoke_client.authentication.validate()
    response.raise_for_status()
    assert response.json()["valid"]


def test_token_authentication_schemes(smoke_client):
    name = "maintenance-" + uuid.uuid4().hex
    response = smoke_client.user_tokens.generate(name=name)
    response.raise_for_status()
    try:
        for scheme in ("bearer", "basic"):
            client = SonarQubeClient(
                smoke_client.host, token=response.json()["token"], token_auth=scheme
            )
            validated = client.authentication.validate()
            validated.raise_for_status()
            assert validated.json()["valid"]
    finally:
        smoke_client.user_tokens.revoke(name=name).raise_for_status()


@pytest.mark.parametrize(
    "provider,create_params,update_params",
    [
        (
            "bitbucket",
            {"url": "http://localhost:9", "personalAccessToken": "test-token"},
            {"url": "http://localhost:9/updated"},
        ),
        (
            "bitbucketcloud",
            {
                "workspace": "test-workspace",
                "clientId": "test-client",
                "clientSecret": "test-secret",
            },
            {"workspace": "updated-workspace", "clientId": "updated-client"},
        ),
        (
            "gitlab",
            {"url": "http://localhost:9", "personalAccessToken": "test-token"},
            {"url": "http://localhost:9/updated"},
        ),
    ],
)
def test_alm_settings_lifecycle(smoke_client, provider, create_params, update_params):
    """Exercise local settings storage without real provider credentials or requests."""
    settings = smoke_client.alm_settings
    key = "api-client-test-" + uuid.uuid4().hex
    renamed = key + "-renamed"
    getattr(settings, f"create_{provider}")(key=key, **create_params).raise_for_status()
    try:
        response = settings.count_binding(almSetting=key)
        response.raise_for_status()
        assert response.json()["projects"] == 0

        getattr(settings, f"update_{provider}")(
            key=key, newKey=renamed, **update_params
        ).raise_for_status()
        key = renamed
        response = settings.count_binding(almSetting=key)
        response.raise_for_status()
        assert response.json()["projects"] == 0
    finally:
        settings.delete_setting(key=key).raise_for_status()

    assert settings.validate(key=key).status_code == 404
