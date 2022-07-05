import numpy as np
from dynarray import DynamicArray
from datetime import datetime
import time
import ftxresponse

def data_writer(data):
    data_matrix.append(np.array([datetime.now().timestamp(), data.get_oi(), data.get_price()]))


if __name__ == "__main__":

    data_matrix = DynamicArray((None, 3))
    data = ftxresponse.Data()
    
    while True:
        data_writer(data)
        time.sleep(60)
        #print(data_matrix)
