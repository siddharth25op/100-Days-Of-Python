import requests
from datetime import datetime

token = "SakuraIsNotTrash!"
username = "siddharth25op"
graphId = "siddharth25op"

params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

pixelaApi = "https://pixe.la/v1/users"

# response = requests.post(url=pixelaApi, json=params)
# print(response.text)

# graphEndpoint = f"{pixelaApi}/{username}/graphs"

# graphConfig = {
#     "id": graphId,
#     "name": "Coding Graph",
#     "unit": "hours",
#     "type": "int",
#     "color": "ajisai"
# }

header = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=graphEndpoint, json=graphConfig, headers=header)
# print(response.text)

PixelPostApi = f"{pixelaApi}/{username}/graphs/{graphId}"

today = datetime.now()

PixelPostParams = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? : ")
}

response = requests.post(url=PixelPostApi, json=PixelPostParams, headers=header)
print(response.text)

UpdateData = f"{PixelPostApi}/20231219"

UpdateParams = {
    "quantity": "4"
}

# response = requests.put(url=UpdateData, json=UpdateParams, headers=header)
# print(response.text)

# response = requests.delete(url=UpdateData, headers=header)
# print(response.text)

