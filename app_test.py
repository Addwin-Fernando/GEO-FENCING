import app  # Import your Flask app module


def test_app():
    client = app.app.test_client()

    # Test if the API returns "working" for the root URL
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_data().decode() == "working"

    # Test if the API returns "inside" for valid data
    response = client.post(
        '/receive_data', json={"center-lat": 80.09734748801102, "center-lon": 12.919357753640268, "lat": 80.09738668239515, "lon": 12.919405460455502})
    assert response.status_code == 200
    assert response.get_data().decode() == "inside"

    # Test if the API returns "outside" for invalid data
    response = client.post(
        '/receive_data', json={"center-lat": 80.09734748801102, "center-lon": 12.919357753640268, "lat": 80.09738668239515, "lon": 13.919405460455502})
    assert response.status_code == 200
    assert response.get_data().decode() == "outside"
