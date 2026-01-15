#!/usr/bin/python3
import urllib, sys
# get url, for example https://httpbin.org/response-headers?X-Request-Id=hello_world and print only the value of X-Request-Id, using a with statement
url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    headers = response.getheaders()
    for header in headers:
        if header[0].lower() == 'x-request-id':
            print(header[1])