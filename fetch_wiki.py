import requests

def get_wikipedia_intro(page_title):
    """
    Fetch the introduction of a Wikipedia page using the MediaWiki API.
    :param page_title: Title of the Wikipedia page to retrieve.
    :return: Introductory text of the page.
    """
    session = requests.Session()
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": page_title,
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
    }
    response = session.get(url=url, params=params)
    data = response.json()
    page = next(iter(data['query']['pages'].values()))
    return page.get('extract', 'No content found.')

# Example usage
print(get_wikipedia_intro("judo"))
# Example usage to fetch information about Michael Jordan
michael_jordan_content = get_wikipedia_intro("Michael Jordan")
print(michael_jordan_content)