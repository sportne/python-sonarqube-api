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
