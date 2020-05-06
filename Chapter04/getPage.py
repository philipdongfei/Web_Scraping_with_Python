import requests
from bs4 import BeautifulSoup

def getPage(url):
    """
    Utilty function used to get a Beautiful Soup object from a given URL
    """
    session = requests.Session()
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
               'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    try:
        req = session.get(url, headers=headers)
    except requests.exceptions.RequestException:
        return None
    bs = BeautifulSoup(req.text, 'html.parser')
    return bs

if __name__ == '__main__':
    html = getPage('http://www.zzrbl.com/')
    print(html)

