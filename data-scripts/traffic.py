import requests
from multiprocessing import Pool, Lock
import pandas as pd
import json

def query(time_interval):
    url = "http://api.hypr.cl/raw/"
    headers = {
     'x-api-key': "iQ0WKQlv3a7VqVSKG6BlE9IQ88bUYQws6UZLRs1B",
     'time_start': time_interval[0], 'time_stop': time_interval[1], 'Accept': "*/*",
     'Cache-Control': "no-cache", 'Host': "api.hypr.cl",
     'Accept-Encoding': "gzip, deflate",
     'Content-Length': "0", 'Connection': "keep-alive",
     'cache-control': "no-cache" }
    response = requests.request("POST", url, headers=headers)
    print(response)
    file = open('trafficData/traffic_'+ time_interval[0].replace(':', '') +'.json', 'w')
    jsonData = json.loads(response.text)
    file.write(json.dumps(jsonData["raw"]))
    file.close()
    print('Processed: ' + str(time_interval))

def main():
    with Pool(20) as pool:
        times = [[("2019-"+str(y).zfill(2)+"-"+str(x).zfill(2)+"T12:00:00Z","2019-"+str(y).zfill(2)+"-"+str(x).zfill(2)+"T12:01:"+"00Z") for x in range(15,30)] for y in range(7, 8)]
        for time in times:
            pool.map(query, time)

if __name__ == "__main__":
    main()


