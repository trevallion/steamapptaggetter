<h2>Introduction</h2>

This is a very simple Python 3.7 module that uses [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) 
and [Requests](https://requests.readthedocs.io/en/master/) to pull the HTML from a Steam app's store page and parse tags 
from the HTML. I made this because (to my knowledge) there is no way to pull Steam app tag data from any of the official
Steam APIs.

<h2>Installation</h2>

I highly recommend installing this as a module in a local virtual environment. However, the contents of 
_steamapptaggetter.py_ should work as long as you have **BeautifulSoup4** and **Requests** (and their respective 
dependencies) installed in your Python environment.

<h2>Usage</h2>
'''python
from steamapppgetter import get_steam_app_tags
app_tags = get_steam_app_tags(730)
''' 