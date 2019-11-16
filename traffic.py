import requests
from multiprocessing import Pool
import pandas as pd
def query(time_interval):
    url = "https://api.hypr.cl/raw/"
    headers = {
     'x-api-key': "**",
     'time_start': "2019-08-01T"+time_interval[0], 'time_stop': "2019-08-01T"+time_interval[1], 'Accept': "*/*",
     'Cache-Control': "no-cache", 'Host': "api.hypr.cl",
     'Accept-Encoding': "gzip, deflate",
     'Content-Length': "0", 'Connection': "keep-alive",
     'cache-control': "no-cache" }
    response = requests.request("POST", url, headers=headers)
    #responsedata = pd.DataFrame(response.text)
    print(response.text)
    return response.text  

p = Pool(16)
f = open('myfile3.txt', 'a')
f.write(p.map(query, [('12:00:00Z','12:00:01Z'),
                    ('12:00:01Z','12:00:02Z'),
                    ('12:00:02Z','12:00:03Z'),
                    ('12:00:03Z','12:00:04Z'),
                    ('12:00:04Z','12:00:05Z'),
                    ('12:00:05Z','12:00:06Z'),
                    ('12:00:06Z','12:00:07Z'),
                    ('12:00:07Z','12:00:08Z'),
                    ('12:00:08Z','12:00:09Z'),
                    ('12:00:09Z','12:00:10Z'),
                    ('12:00:10Z','12:00:11Z'),
                    ('12:00:11Z','12:00:12Z'),
                    ('12:00:12Z','12:00:13Z'),
                    ('12:00:13Z','12:00:14Z'),
                    ('12:00:14Z','12:00:15Z'),
                    ('12:00:15Z','12:00:16Z')])
f.close()


