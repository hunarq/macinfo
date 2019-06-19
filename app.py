import os
import argparse
import requests

API_KEY = ''

def get_mac(mac):
    url = 'https://api.macaddress.io/v1?apiKey=' + API_KEY + '&output=json&search=' + mac
    resp = requests.get(url)

    js = resp.json()
    print({'companyName': js['vendorDetails']['companyName']})


parser = argparse.ArgumentParser(description="MAC-INFO CLI")
parser.add_argument(
    '--mac',
    help='MAC Address to search',
)
args = parser.parse_args()

if __name__ == "__main__":
    print(args)
    if args.mac:
        API_KEY = os.environ['API_KEY']
        get_mac(args.mac)
    else:
        parser.print_help()
