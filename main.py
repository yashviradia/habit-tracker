import requests
import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime

load_dotenv(find_dotenv())

today = datetime(year=2021, month=12, day=21)


USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
GraphID = os.environ.get("GraphID")
DATE = today.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

user_response = requests.post(pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GraphID,
    "name": "Book Graph",
    "unit": "minutes",
    "type": "int",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Post a pixel in the graph
pixel_post_endpoint = f"{graph_endpoint}/{GraphID}"


pixel_post_params = {
    "date": DATE,
    "quantity": input("How long did you read book today? "),
}

pixel_post_response = requests.post(url=pixel_post_endpoint, json=pixel_post_params, headers=headers)
# print(pixel_post_response.text)

# Edit the pixel using put request
edit_pixel_endpoint = f"{pixel_post_endpoint}/{DATE}"

edit_pixel_params = {
    "quantity": "360",
}

# edit_pixel_response = requests.put(edit_pixel_endpoint, json=edit_pixel_params, headers=headers)
# print(edit_pixel_response.text)

# Delete the pixel using delete request
delete_pixel_endpoint = f"{edit_pixel_endpoint}"

