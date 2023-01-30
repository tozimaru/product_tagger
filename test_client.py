import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input', type=str)
args = parser.parse_args()

text = args.input
data = {'text': text}

resp = requests.post('http://0.0.0.0:5001/process_one', data=json.dumps(data), headers={'content-type': 'application/json'})
print(resp.text)