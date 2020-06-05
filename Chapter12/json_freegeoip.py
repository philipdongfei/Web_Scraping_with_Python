#!/usr/bin/env python3
# freegeoip shutdown 2018

import json
from urllib.request import urlopen

def getCountry(ipAddress):
    response = urlopen('http://freegeoip.net/json'+ipAddress).read()
        .decode('utf-8')
    responseJson = json.load(response)
    return responseJson.get('country_code')

print(getCountry('50,78.253.58'))


