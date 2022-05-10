def test_registration(client):
    response = client.get("/register")
    assert b'href="/login"' in response.data
    response = client.post("/register", data={
        "email": "test@mail",
        "password": "testpassword"
    })
    assert b'href="/register"' in response.data
    assert response.status_code == 200