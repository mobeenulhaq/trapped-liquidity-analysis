import ftxresponse
from datetime import datetime
import csv
import time

class FileWriter:

    def __init__(self, filename) -> None:
        self.filename = filename

    # file appending function
    def fileAppend(self, data):
        #data = test2.Data()

        with open(self.filename, 'a', newline="") as f:
            writer = csv.writer(f)
            now = datetime.now()
            writer.writerow([now.timestamp(), data.get_price(), data.get_oi()])

if __name__ == "__main__":

    path = 'btc-data.csv'
    fwriter = FileWriter(path)
    data = ftxresponse.Data()
    
    while True:
        fwriter.fileAppend(data)
        time.sleep(1)

    
