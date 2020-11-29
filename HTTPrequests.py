#!/usr/bin/env python

import requests
import os

#url = "http://www.pudim.com.br/"

'''
    if "Extension not allowed" in r.text:
        print(f"{ext} not allowed")
    else:
        print(f"{ext} SEEMS TO BE ALLOWED??")
    
    old_filename = new_filename

'''
#r = requests.post(url, files=files)
#r.post('https://httpbin.org/post', data={'key':'value'})
#json_r = response.json()
#cookies = {'enwiki_session': '17ab96bd8ffbe8ca58a78657a918558'}
#r = requests.post('http://wikipedia.org', cookies=cookies)
#print(r.headers['content-type'])
#print(r.encoding)


# Set IP target and set Port and Set url target
ip = "10.10.61.85"
path = "/ctf/sendcookie"
url = f"http://{ip}:8081{path}"
cookies = {"flagpls":"flagpls"}

#r = requests.get(url)
#r = requests.post(url, data="flag_please")
#r = requests.get(url)
r = requests.get(url, cookies=cookies)
print(r.status_code)
print(r.text)
#print(r.cookies)

