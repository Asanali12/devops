"""
Testing time api
"""
import requests


def test_time(client):
    """
    Tests time api
    """
    response_api = requests.get(
        'https://www.timeapi.io/api/Time/current/coordinate?latitude=55.45&longitude=37.36')
    if response_api.status_code == 200:
        payload = response_api.json()
        expected = "Moscow time:" + \
            str(payload["hour"])+":"+str(payload["minute"]) + \
            ":"+str(payload["seconds"])
    else:
        expected = "not passed"
    response = client.get('/')
    assert response.status_code == 200
    assert expected == response.get_data(as_text=True)
