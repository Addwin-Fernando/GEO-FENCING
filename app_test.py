import app 


def test_app():
    client = app.app.test_client()

    # Test if the API returns "working" for the root URL
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_data().decode() == "Locked"

    # Test if the API returns "Unlocked" for valid data
    response = client.post(
        '/receive_data', json={"center-lat": 80.09734748801102, "center-lon": 12.919357753640268, "lat": 80.09738668239515, "lon": 12.919405460455502})
    assert response.status_code == 200
    assert response.get_data().decode() == "Unlocked"

    # Test if the API returns "Locked" for invalid data
    response = client.post(
        '/receive_data', json={"center-lat": 80.09734748801102, "center-lon": 12.919357753640268, "lat": 80.09738668239515, "lon": 13.919405460455502})
    assert response.status_code == 200
    assert response.get_data().decode() == "Locked"
