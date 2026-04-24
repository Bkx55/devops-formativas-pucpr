from app import APP_MESSAGE, app


def test_home_returns_200():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_home_returns_json_content_type():
    client = app.test_client()
    response = client.get("/")
    assert response.is_json is True


def test_home_message_value():
    client = app.test_client()
    response = client.get("/")
    payload = response.get_json()
    assert payload["message"] == APP_MESSAGE


def test_home_status_value():
    client = app.test_client()
    response = client.get("/")
    payload = response.get_json()
    assert payload["status"] == "ok"


def test_health_endpoint_returns_healthy_true():
    client = app.test_client()
    response = client.get("/health")
    payload = response.get_json()
    assert response.status_code == 200
    assert payload["healthy"] is True


def test_post_method_not_allowed_in_home():
    client = app.test_client()
    response = client.post("/")
    assert response.status_code == 405
