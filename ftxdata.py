from sqlite3 import Row
import numpy as np
from dynarray import DynamicArray
from datetime import datetime
import time
import ftxresponse
import csv

def data_writer(data):
    data_matrix = DynamicArray((None, 3))

    while True:
        data_matrix.append(np.array(data))


if __name__ == "__main__":

    data = ftxresponse.Data()
    
    while True:
        
        time.sleep(1)
