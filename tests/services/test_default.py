def test_whenGettingRoot_thenReturnsHelloWorld(client):
    r = client.get('/')
    data = r.json()

    assert data == "Hello World!"
