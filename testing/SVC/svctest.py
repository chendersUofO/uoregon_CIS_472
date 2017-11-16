import sys
import json
from PyML import *

f = json.load(open('train.json'))


Catigories = []
for Keyword in f:
    KW_list = Keyword['cuisine']
    for text_dict in KW_list:
        Catigories = text_dict['ingredients']
