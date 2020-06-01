import requests

files = {'uploadFile': open('files/python.png', 'rb')}
# post url diff book example
r = requests.post('http://www.pythonscraping.com/pages/files/processing2.php', files=files)
print(r.text)

