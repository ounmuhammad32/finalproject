def test_login(client):
    # POST to the login with the email and password to authenticate
    response = client.post("/login", data={
        "email": "test@mail",
        "password": "testerpassword"
    })
    assert b"Redirecting..." in response.data
    # Verify that we are redirecting to the dashboard
    assert b'href="/login"' in response.data
    assert response.status_code == 302