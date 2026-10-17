import pytest

from sonarqube import SonarQubeClient


def test_token_uses_bearer_authentication():
    client = SonarQubeClient("http://localhost:9000", token="example")
    assert client.session.headers["Authorization"] == "Bearer example"
    assert client.session.auth is None


def test_basic_token_authentication_remains_available():
    client = SonarQubeClient(
        "http://localhost:9000", token="example", token_auth="basic"
    )
    assert client.session.auth == ("example", "")
    assert "Authorization" not in client.session.headers


def test_invalid_token_authentication_is_rejected():
    with pytest.raises(ValueError, match="token_auth"):
        SonarQubeClient("http://localhost:9000", token="example", token_auth="invalid")
