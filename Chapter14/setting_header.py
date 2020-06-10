import requests
from bs4 import BeautifulSoup

session = requests.Session()
'''
# PC devices browsing headers
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'\
           'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept': 'text/html,application/xhtml+xml,application/xml;'\
           'q=0.9,image/webp,*/*;q=0.8'}
'''
# mobile devices browsing headers
headers = {'User-Accept':'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X)'\
           'AppleWebKit 537.36 (KHTML, like Gecko)',
           'Version':'7.0','Mobile':'11D257','Safari':'9537.53',
           'Accept': 'text/html,application/xhtml+xml,application/xml;'\
           'q=0.9,image/webp,*/*;q=0.8'}

url = 'https://www.whatismybrowser.com/'\
    'developers/what-http-headers-is-my-browser-sending'
req = session.get(url, headers=headers)

bs = BeautifulSoup(req.text, 'html.parser')
print(bs.find('table', {'class':'table-striped'}).get_text)


