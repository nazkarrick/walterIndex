import requests
import json
import follium
# from datetime import datetime
"""
API functionality testing,
PYTHON json filtering methods
"""



# def jprint(obj):
#     # create a formatted string of the PYTHON json object
#     # dumps() = takes a PYTHON obj, and converts it to a string
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)
# response = requests.get('http://api.open-notify.org/iss-now.json')

# jprint(response.json())
# for loop to print keys in object
# iss = response.json()
# for keys in iss:
#     print(keys)
# cd = iss['iss_position']
# unxt = iss['timestamp']
# print(cd)
# print(unxt)

# Determine best practice to format unix timestamp.????
# standardTime = []
# time = datetime.fromtimestamp(cd)
# standardTime.append(time)
# print(standardTime)

# jprint(iss['iss_position'])

########===== MAIL LIST API TEST =====##########
# from mailjet_rest import Client
# import os
# api_key = '05a8c6a9bd9006ba756f22db838ae3fc'
# api_secret = '1c1559462c80b9c203c1b7c10c3eee76'
# mailjet = Client(auth=(api_key, api_secret), version='v3.1')
# data = {
#     'Messages': [
#             {
#             "From": {
#                 "Email": "designed.x.horo@gmail.com",
#                 "Name": "Robert"
#             },
#             "To": [
#                 {
#                 "Email": "designed.x.horo@gmail.com",
#                 "Name": "Robert"
#                 }
#             ],
#             "Subject": "Greetings from Mailjet.",
#             "TextPart": "My first Mailjet email",
#             "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
#             "CustomID": "AppGettingStartedTest"
#             }
#     ]
# }
# result = mailjet.send.create(data=data)
# print(result.status_code)
# print(result.json())