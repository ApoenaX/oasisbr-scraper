import functools
import urllib.parse

import requests

API_URL = "https://oasisbr.ibict.br/vufind/api/v1/"


@functools.lru_cache(maxsize=128)
def requests_get(url):
    """Wrapper para requests.get que faz cache dos resultados."""
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def access_endpoint(
    endpoint: str = "search",
    params: dict | None = None,
) -> dict:
    """Accesses the OASISBR API endpoint and returns the response as a dict.

    Args:
        endpoint (str): The API endpoint to be accessed.
        params (dict): A dictionary containing the parameters to be passed to the endpoint.

    Returns:
        dict: The response from the API endpoint as a dict.

    Note:
        The API response is cached using functools.lru_cache. The cache is cleared
        when the function is called with different parameters. The cache is limited
        to 128 entries.

        See https://oasisbr.ibict.br/vufind/api/v1/ for a list of available endpoints and parameters.
    """
    if params is None:
        params = {}
    url = f"{urllib.parse.urljoin(API_URL, endpoint)}?{urllib.parse.urlencode(params, doseq=True)}"
    return requests_get(url)
