# product_tagger

## Product name parts tagging
We utilize a NER tagger with custom labels to extract useful information from a generic entry in retail data. As a test run, initial dataset included 415 entries for training set, and 48 for validation set. The custom labels are: BRAND_NAME, PRODUCT_NAME, ADJ, SIZE, MISC

### Pre-requisites
* Python>=3.8
* CUDA 10.2

### Requirements
* Pytorch 1.12.1
* spacy v3.5 (with transformers and cuda)
* flask
* label-studio

*The code may work on other versions of torch/cuda. The specified version are merely the latest tested versions.*

### Installation note

It should work with other version of CUDA, as long as your torch version supports your installed version. 

`pip install -r requirements.txt`

### Usage
Download the trained multilingual spacy model from this [link](https://drive.google.com/file/d/1HQNJZBaRLU4NpQXbLccF1GcdGP4jz9wf/view?usp=share_link)

And extract inside a directory name `output` under project root. If extracted elsewhere, just use the argument `--model_dir <path-to-model-directory>` when initializing `ner_engine.py`.

Local server can be turned on `localhost:5001` by running `ner_engine.py`. For local usage, plain flask server should work fine. 

Turn on: `python ner_engine.py`. API could be sped up by using a different backend for the server such as gunicorn. In such case, you may use: `gunicorn --workers <NUM_OF_WORKERS> --bind 0.0.0.0:5001 ner_engine:app`

The server currently has single endpoint for processing sentences one by one: 
   address: `0.0.0.0:5001/process_one`  
   receives: `{"text": string}`, returns: `{"words": list, "labels": list}`


### Training

#### Data prep
Use label studio to annotate data. Make sure to use "CONLL2003" format when exporting. After exporting use:
`python -m spacy convert <path-to-conll-file> . --converter conll` to generate .spacy file. It is advised to generate separate file for validation as well. 

#### Run training
The provided base_config and config files should be sufficient for any amount of data. A change will only be needed if other pipelines are to be added.

Run `python -m spacy train config.cfg --output ./output --paths.train ./corpus/train.spacy --paths.dev ./corpus/dev.spacy --gpu-id 1` to train.

### TODO

* Batch processing
* ~~Train a production model with at least 3000 training data.~~ New weights uploaded.
