import numpy as np
import tensorflow as tf
from tensorflow import keras
from matplotlib import pyplot as plt
import csv
from pprint import pprint

def read_data():
    res = read_csv('data/romance.csv')
    print(len(res))
    


def read_csv(file_name):
    res = []
    with open(file_name, 'r') as f:
        rows = csv.reader(f)
        rows = [row for row in rows]
        head = rows[0]
        rows = rows[1:]
        for row in rows:
            tmp = dict()
            for i in range(len(head)):
                try:
                    tmp[head[i]] = row[i]
                except IndexError:
                    pass
            res.append(tmp)
    
    return res 


read_data()