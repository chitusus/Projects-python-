import requests
import json

def get_ticket():
    requests.packages.urllib3.disable_warnings() # disable ssl warning

    # TICKET API URL
    api_url = 'https://sandboxapicem.cisco.com/api/v1/ticket'

    # ALL APIC-EM REST API request and response content type is json
    headers = {
        'Content-Type':'application/json'
    }
    # JSON input body content
    body_json = {
        'password':'Cisco123!',
        'username':'devnetuser'
    }
    # Make request and get response "resp" is the response of this request
    resp = requests.post(api_url, json.dumps(body_json),headers=headers,verify=False)

    # Create object to contain the request status
    print('Ticket request status', resp.status_code) # display the response code

    # Create object to contain converted json-formatted response
    response_json = resp.json()

    # Parse data fo service ticket
    service_ticket = response_json['response']['serviceTicket']

    # Display service ticket value
    print('The service ticket number is',service_ticket)

    return service_ticket


get_ticket()












# url = "https://sandboxapicem.cisco.com/api/v1/ticket"
# url_new = 'https://api.github.com'
# payload = {"password": "Cisco123!","username": "devnetuser"}
#
# headers = {'Content-Type':'application/json'}
# res = requests.post(url, json.dumps(payload), headers=headers)
#
# response = requests.get(url_new)
# print(response.headers['Content-Type'])
# response.headers['Content-Type']
# response.headers
# print(res.text.encode('utf8'))

# response=response.json()
#
# for i in response:
#     print(i)
# print(response)
