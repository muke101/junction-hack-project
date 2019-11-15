import requests as r

data = r.get("https://micromec.org:32001").json() 

#MAC:humidity,temperature,pressure,isRaining,isIcy
dbFormat = {}

acceptedValues = ['humidity', 'temperature', 'pressure']

for pi in data:
    values = []
    for field in data[pi]:
        if field in acceptedValues:
            values.append(data[pi][field])
        dbFormat[pi] = values
    if data[pi]['humidity'] > 80 and data[pi]['pressure'] < 1022:
        dbFormat[pi].append(True)
        if data[pi]['temperature'] < 0:
            data[pi].append(True)
        else:
            data[pi].append(False)
    else:
        data[pi].append(False, False)

