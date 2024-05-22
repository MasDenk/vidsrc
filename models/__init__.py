from .subtitle import subfetch
VERSION = '3.0.0'
from .vidsrcme import get as vidsrcmeget
from .vidsrcto import get as vidsrctoget
from .utils import fetch
# UTILS
async def info():
    return {
    "project":"vidsrc-scrape-api",
    "note":"This api is made for educational purpouse only.",
    "version": VERSION,
    "developer":"MasDenk"
    }
