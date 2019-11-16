import requests
from multiprocessing import Pool, Lock
import pandas as pd

def query(time_interval):
    url = "https://api.hypr.cl/raw/"
    headers = {
     'x-api-key': "iQ0WKQlv3a7VqVSKG6BlE9IQ88bUYQws6UZLRs1B",
     'time_start': "2019-08-01T"+time_interval[0], 'time_stop': "2019-08-01T"+time_interval[1], 'Accept': "*/*",
     'Cache-Control': "no-cache", 'Host': "api.hypr.cl",
     'Accept-Encoding': "gzip, deflate",
     'Content-Length': "0", 'Connection': "keep-alive",
     'cache-control': "no-cache" }
    response = requests.request("POST", url, headers=headers)
    #responsedata = pd.DataFrame(response.text)
    #print(response.text)
    with lock:
        file.write('"' + time_interval[0] + '":' + response.text + ',')
        print('Processed: ' + str(time_interval))


def init_child(lock_, file_):
    global lock
    lock = lock_
    global file
    file = file_

def main():
    lock = Lock()
    file = open('gotValues.json', 'a')
    file.truncate(0)
    file.write('{')
    with Pool(59, initializer=init_child, initargs=(lock, file)) as pool:
        times = list(map(lambda x: ('12:'+ str(x).zfill(2) +':00Z','12:'+ str(x).zfill(2) +':59Z'), range(59)))
        pool.map(query, times)
    file.write('}')
    file.close()

if __name__ == "__main__":
    main()


