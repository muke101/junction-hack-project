import requests
from multiprocessing import Pool, Lock
import pandas as pd
import json

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
    file = open('trafficData/traffic_'+ time_interval[0].replace(':', '') +'.json', 'w')
    jsonData = json.loads(response.text)
    file.write(json.dumps(jsonData["raw"]))
    file.close()
    print('Processed: ' + str(time_interval))

def main():
    with Pool(20) as pool:
        times = [[(str(y).zfill(2)+':'+str(x).zfill(2)+':00Z',str(y).zfill(2)+':'+str(x+1).zfill(2)+':'+'00Z') for x in range(0,59,5)] for y in range(24)]
        for time in times:
            pool.map(query, time)

if __name__ == "__main__":
    main()


