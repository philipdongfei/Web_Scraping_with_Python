import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('philip', 'password')
session = requests.Session()

s = session.post(
    url='http://pythonscraping.com/pages/auth/login.php',auth=auth
)
print(s.text)

