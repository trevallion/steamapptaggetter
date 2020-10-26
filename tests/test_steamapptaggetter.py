from steamapptaggetter import SteamAppTagGetter


def test_get_app_tags():
    html = """<html><body><a href="" class="app_tag" style="display: none;">
                                                FPS </a><a href="" class="app_tag" style="display: none;">
                                                Shooter </a><a href="" class="app_tag" style="display: none;">
                                                Multiplayer </a><a href="" class="app_tag" style="display: none;">
                                                Moddable </a><div class="app_tag add_button">+</div>
                                                </body></html>"""
    tags_in_html = ['FPS', 'Shooter', 'Multiplayer', 'Moddable']
    tag_getter = SteamAppTagGetter(html)
    app_tags = tag_getter.get_app_tags()

    assert set(tags_in_html) == set(app_tags)
