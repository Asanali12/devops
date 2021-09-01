"""
Testing availability
"""


def test_time(client):
    """
    Tests availability
    """
    assert client.get("http://127.0.0.1:8080"), "Unreached."