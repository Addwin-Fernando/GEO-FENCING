import app  # Import your Flask app module


def test_app():
    client = app.app.test_client()

    # Test if the API returns "working" for the root URL
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_data().decode() == "working"

    # Test if the API returns "inside" for valid data
    response = client.post(
        '/receive_data', json={"center-lat": 0, "center-lon": 0, "lat": 1, "lon": 1})
    assert response.status_code == 200
    assert response.get_data().decode() == "inside"

    # Test if the API returns "outside" for invalid data
    response = client.post(
        '/receive_data', json={"center-lat": 0, "center-lon": 0, "lat": 10, "lon": 10})
    assert response.status_code == 200
    assert response.get_data().decode() == "outside"
