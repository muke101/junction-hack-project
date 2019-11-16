import requests
import pandas as pd
url = "https://api.hypr.cl/raw/"
headers = {
 'x-api-key': "**",
 'time_start': "2019-08-01T12:00:00Z", 'time_stop': "2019-08-01T12:01:00Z", 'Accept': "*/*",
 'Cache-Control': "no-cache", 'Host': "api.hypr.cl",
 'Accept-Encoding': "gzip, deflate",
 'Content-Length': "0", 'Connection': "keep-alive",
 'cache-control': "no-cache" }
response = requests.request("POST", url, headers=headers)
#responsedata = pd.DataFrame(response.text)
print(response.text)
file1 = open("myfile3.txt","w") 
L = response.text  

file1.write(L) 
file1.close() #to change file access modes 


