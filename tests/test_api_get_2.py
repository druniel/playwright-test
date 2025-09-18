def test_api_get(playwright):
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept": "application/json",
            "X-Api-Key": "reqres-free-v1"
        }
    )
    response = request.get("http://127.0.0.1:8000/users")
    assert response.status == 200
    json_data = response.json()
    print(json_data)
    
    request.dispose()
    print("Test completed successfully.")