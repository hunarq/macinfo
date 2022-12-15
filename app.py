import os

import logging
import requests
from flask import Flask, make_response

API_KEY = ''

def get_mac(mac):
    url = 'https://api.macaddress.io/v1?apiKey=' + API_KEY + '&output=json&search=' + mac
    resp = requests.get(url)

    js = resp.json()
    if "error" in js:
        print(f"Error:{js}")
        return ""
    else:
        return js['vendorDetails']['companyName']


app = Flask(__name__)


@app.route('/api/<mac>')
def api(mac):
    company = ""
    try:
        print(mac)
        company = get_mac(mac)
    except Exception as e:
        print(e)

    resp = make_response('{"CompanyName": "' + company + '" }', 200)
    resp.mimetype = 'application/json'
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == '__main__':
    API_KEY = os.environ.get("API_KEY", "")
    app.run(debug=True, host='0.0.0.0', port=8080)

