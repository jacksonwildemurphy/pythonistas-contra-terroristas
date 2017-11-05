#!/bin/bash
pip install --user virtualenv

mkdir venv

python -m virtualenv venv #for python2.7

##python -m virtualenv venv -p /home/rachmani/python3.5/bin/python3.5 #for python3.5

source venv/bin/activate

pip install spacy

python -m spacy download en

python ie.py $1
#######Commands for python3.5
#python3.5 -m pip install --user spacy
#python3.5 -m spacy.en.download all
#python3.5 ie.py "$1"