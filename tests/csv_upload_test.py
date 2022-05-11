# This test checks if the transactions csv file exists within the upload folder:
def test_csv_upload(client):
    file = "./app/uploads/transactions.csv"
    data = {'file': (open(file, 'rb'), file)}

    # once the login test works I copy that code here for logging in
    res = client.get("/login")
    assert res.status_code == 200