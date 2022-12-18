
import numpy as np
from pathlib import Path
from tqdm import tqdm
import os
import shutil
from music21 import *
import sys
from pymongo import MongoClient


mongo = MongoClient(host='hyerin',
                     port=36000, 
                    authSource="admin")

dbNames = mongo.list_database_names()

if sys.argv[1] == 'dbNames':
  for each in dbNames:
    print(each)

elif sys.argv[1] == 'collectionNames':
  collectionNames = mongo[sys.argv[2]].list_collection_names()
  for each in collectionNames:
    print(each)
    

if __name__ == '__main__':
    data_dir = input()
    c = converter.parse(data_dir)
    tonal = c.analyze('key').name.split(' ')[-1]

    if tonal != 'major':
        print("False") #minor
    else:
        print("True") #major
