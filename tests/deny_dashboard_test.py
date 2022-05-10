def test_deny_dashboard(client):
    # POST to the login with the email and password to authenticate
    response = client.get("/dashboard")
    assert b"Redirecting..." in response.data
    # Verify that we are redirecting to the dashboard
    assert b"/login" in response.data
    assert response.status_code == 302