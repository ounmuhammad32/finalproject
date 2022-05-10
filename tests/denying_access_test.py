def test_denying_access(client):
    """This makes the index page"""
    response = client.get("/login")
    assert response.status_code == 200
    # POST to the login with the email and password to authenticate
    response = client.post("/login", data = {
        "email": "test@test",
        "password": "wrongpassword"
    })
    assert b"Redirecting..." in response.data
    # Make sure we are redirecting back to the login screen.
    assert b'href="/login"' in response.data
    assert response.status_code == 302