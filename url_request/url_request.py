import requests


def request_url(url):
    """Send request for the given url. Raise the status of the request."""

    response = requests.get(url=url)
    response.raise_for_status()
