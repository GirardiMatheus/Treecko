def test_create_account(test_client):
    response = test_client.post(
        "/api/v1/accounts/",
        json={"name": "Emergency Fund", "account_type": "emergency", "balance": 500.0}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Emergency Fund"
    assert data["account_type"] == "emergency"
    assert data["balance"] == 500.0

def test_get_account(test_client):
    response = test_client.get("/api/v1/accounts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Emergency Fund"
