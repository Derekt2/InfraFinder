#!/usr/bin/python3

import flatten_json
from secrets import api_key, secret
import censys.ipv4
import re
from sys import argv
from defang import refang
import argparse

parser = argparse.ArgumentParser(prog="infrafinder.py", description='Find related attributes among ip addresses as censys queries. Set api key and secret in secrets.py')
parser.add_argument('IP', help='IP address to compare', nargs='+')
parser.add_argument('--exclude', '-e', help='exclude attributes from a false positive', nargs='+')
args = parser.parse_args()

#setting our credentials and getting ready to use censys API
c = censys.ipv4.CensysIPv4(api_id=api_key, api_secret=secret)

#declare a patern to fix the deep nested syntax flatten_json uses
pattern = re.compile(r"\.\d+")

# define function to refang arguments if needed
def refang_args(arguments):
    for x, y in enumerate(arguments):
        if '[.]' in arguments[x]:
            arguments[x] = refang(arguments[x])

#define function to lookup and process the deeply nested JSON
def lookup_flat(IP):
    json = flatten_json.flatten(c.view(IP), '.')
    list_result = []
    json_to_list(json, list_result)
    return list_result

#defining a function that modifies a JSON object into a list and modifies the keys to their original state
def json_to_list(start_json, result_list):
    for key in start_json:
        fixed_key = pattern.sub("", key)
        result_list.append(f'{fixed_key}:\"{start_json[key]}\"')

#define main function that refangs arguments, and compares resulting JSON list to find matching criteria
if __name__ == "__main__":
    refang_args(args.IP)
    result = set(lookup_flat(args.IP[0]))
    for x in args.IP[1:]:
        result &= set(lookup_flat(x))
    if args.exclude:
        for x in args.exclude[0:]:
            result -= set(lookup_flat(x))
    for value in sorted(result):
        print(f"{value} AND")