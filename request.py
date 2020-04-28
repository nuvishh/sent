import requests

url = 'http://localhost:5000/clas'
r = requests.post(url,json={'text':'മോശം'})

print(r.json())
