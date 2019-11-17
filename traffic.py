import requests
from multiprocessing import Pool, Lock
import pandas as pd
import json

from os.path import join

def query(time_interval):
    print('Starting with {}'.format(time_interval))
    url = "https://api.hypr.cl/raw/"
    headers = {
     'x-api-key': "iQ0WKQlv3a7VqVSKG6BlE9IQ88bUYQws6UZLRs1B",
     'time_start': "2019-08-01T"+time_interval[0], 'time_stop': "2019-08-01T"+time_interval[1], 'Accept': "*/*",
     'Cache-Control': "no-cache", 'Host': "api.hypr.cl",
     'Accept-Encoding': "gzip, deflate",
     'Content-Length': "0", 'Connection': "keep-alive",
     'cache-control': "no-cache" }
    response = requests.request("POST", url, headers=headers)
    rjson = response.json()
    #responsedata = pd.DataFrame(response.text)
    #print(response.text)
    
    with open(join('traffic', 'values__{}__{}.raw'.format(*time_interval)), 'w+') as f:
        #f.write(response['raw'])
        json.dump(rjson, f)
        #f.write(rjson)
        print('Processed: {}'.format(time_interval))

#    with lock:
#        file.write(response['raw'])
#        #file.write('"' + time_interval[0] + '":' + response.text + ',')
#        print('Processed: ' + str(time_interval))


def init_child(lock_=None, file_=None):
    global lock
    lock = lock_
#    global file
#    file = file_

def main():
    lock = Lock()
#    file = open('gotValues.json', 'a')
#    file.truncate(0)
#    file.write('[')
#    with Pool(100, initializer=init_child, initargs=(lock, file)) as pool:
    with Pool(2, initializer=init_child, initargs=(lock,)) as pool:
        times = [[(str(y).zfill(2)+':'+str(x).zfill(2)+':00Z',str(y).zfill(2)+':'+str(x+1).zfill(2)+':'+'00Z') for x in range(0,59,5)] for y in range(24)]
        for time in times:
            pool.map(query, time)
#    file.write('}')
#    file.close()

if __name__ == "__main__":
    main()


