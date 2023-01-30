import os
import sys
import json
import random

import spacy
from flask import Flask, Response, request

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--model_dir', type=str, default='./output/model-best', help='path to spacy trained model')
args = parser.parse_args()

def load_model(args):
    #load the spacy model, currently the model only has NER and Transformer pipelines
    global nlp
    nlp = spacy.load(args.model_dir)
    return

app = Flask(__name__)

@app.route('/process_one', methods=['POST'])
def process():
    data = request.get_json()
    text = data['text']
    doc = nlp(text)
    
    result = {'words': [], 'labels': []}
    for token in doc.ents:
        result['words'].append(token.text)
        result['labels'].append(token.label_)
    
    return Response(json.dumps(result), status=200, headers={'content-type': 'application/json'})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5001)
    


