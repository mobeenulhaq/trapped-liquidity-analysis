import ftxdata
from datetime import datetime
import asyncio
import csv

class FileWriter:

    def __init__(self, filename) -> None:
        self.filename = filename

    # file appending function
    async def fileAppend(self, data):
        #data = test2.Data()

        with open(self.filename, 'a', newline="") as f:
            writer = csv.writer(f)
            while True:
                now = datetime.now()
                await asyncio.sleep(60) # data needs to be plotted and analysed per 6o seconds
                writer.writerow([now, data.get_price(), data.get_oi()])

if __name__ == "__main__":

    path = ''
    fwriter = FileWriter(path)
    data = ftxdata.Data()

    loop = asyncio.get_event_loop()

    try:
        asyncio.ensure_future(fwriter.fileAppend(data))
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()
