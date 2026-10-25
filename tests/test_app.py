from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"CI/CD Cloud App" in response.data


def test_health():
    client = app.test_client()
    response = client.get("/health")
    data = response.get_json()
    assert response.status_code == 200
    assert data["status"] == "ok"


def test_unknown_route():
    client = app.test_client()
    response = client.get("/not-found")
    assert response.status_code == 404


# Індивідуальний тест варіанта 7 (СТО): endpoint /api/orders
def test_orders():
    client = app.test_client()
    response = client.get("/api/orders")
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) == 3
    assert data[0]["id"] == 1
    assert data[0]["service"] == "Заміна масла"
