from urllib import request, response
import requests


BASE = "http://127.0.0.1:5000/"

# data =[
#     {"likes":10,"name":"Heidy","views":10},
#     {"likes":10,"name":"Nor","views":10},
#     {"likes":10,"name":"Vapp","views":10}
# ]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

response = requests.patch(BASE + "video/2",{"views":99,"likes":100})
print(response.json())