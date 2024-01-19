#======SINCH-OTP Validation======#

import requests

def send_request(phonenumber):
  url = "https://verificationapi-v1.sinch.com/verification/v1/verifications"
  payload="{\n  \"identity\": {\n  \"type\": \"number\",\n  \"endpoint\": \"+91"+format(phonenumber)+"\"\n  },\n  \"method\": \"sms\"\n}"
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ZmE2MzVlZmYtZDVlZS00ODhjLTgxZDktNjQzYmU5N2IzNGM4OnE1SVo3ckZwdjBHaEJ3cWdEbWRtVmc9PQ==',
    'Accept-Language': 'en-US'
  }
  response = requests.post(url, headers=headers, json=payload)
  return response.ok


def verify_Otp(OTP, phonenumber):
  url = "https://verificationapi-v1.sinch.com/verification/v1/verifications/number/+91"+phonenumber
  payload="{ \"method\": \"sms\", \"sms\":{ \"code\": \""+format(OTP)+"\"}}"
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ZmE2MzVlZmYtZDVlZS00ODhjLTgxZDktNjQzYmU5N2IzNGM4OnE1SVo3ckZwdjBHaEJ3cWdEbWRtVmc9PQ==',
  }
  response = requests.put(url, headers=headers, json=payload)
  return response.ok