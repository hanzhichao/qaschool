import requests
from tomd import Tomd
import re

def url_to_md(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3590.0 Safari/537.36'}
    html = requests.get(url, headers=headers, verify=False).text
    md = Tomd(html).markdown
    return md


