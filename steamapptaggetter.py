from bs4 import BeautifulSoup
import requests


def get_steam_app_url(app_id):
    """
    Get URL for app's Steam store page.
    :param app_id: Steam store app id
    :return: Steam Store URL for given app id.
    """
    return f'https://store.steampowered.com/app/{app_id}'


def get_steam_app_html(app_id):
    """
    Get html from Steam app's Steam store page.
    :param app_id: Steam Store app id
    :return: html string from Steam store page.
    """
    url = get_steam_app_url(app_id)
    request = requests.get(url)
    return request.text


def get_steam_app_tags(app_id):
    """
    Get all user-defined app tags from a Steam app's store page.
    :param app_id: Steam Store app id
    :return: list of app tags
    """
    html = get_steam_app_html(app_id)
    tag_getter = SteamAppTagGetter(html)
    tags = tag_getter.get_app_tags()
    return tags


class SteamAppTagGetter:
    def __init__(self, html):
        self.html = html

    def get_app_tags(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        app_tags = []
        for parsed_tag in soup.find_all(class_="app_tag"):
            app_tag = "".join(parsed_tag.contents).strip()
            if app_tag != '+':
                app_tags.append(app_tag)

        return app_tags
