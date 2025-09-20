def test_api_post(playwright):
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept": "application/json",
            "Authorization": "Bearer YOUR_ACCESS_TOKEN",
            "X-Api-Key": "reqres-free-v1"
        }
    )
    response = request.post("http://127.0.0.1:8000/items", data={"id": 5, "name": "Daniel"})
    assert response.status == 201
    print(response.json())
    request.dispose()