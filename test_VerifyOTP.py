import json
from unittest import TestCase
import pytest
import requests
import EnvironmentRead


class VerifyOTP(TestCase):
    def setUp(self):
        print("this is verify OTP setup")

    def tearDown(self):
        print("this is verify OTP tear down")

    @pytest.mark.run(order=4)
    def test_Verify_OTP(self):
        with open('responsedata.json') as f:
            applicationId = json.loads(f.read())
            applicationId = applicationId['applicationId']
            print(applicationId)

        url = str(
            EnvironmentRead.ipPort) + "/v1/users/" + applicationId + "/register/verify/otp?access_token={0}".format(
            EnvironmentRead.access_token)

        with open('responsedata.json') as f:
            sessionKey = json.loads(f.read())
            sessionKey = sessionKey['sessionKey']
            print(sessionKey)

        headers = {'Content-type': 'application/json', 'SessionKey': sessionKey}

        with open('otp.json') as f:
            otp = json.loads(f.read())
            otp = otp['otp']
            print(otp)
            body = {
                'otp': otp,
                'mobileNumber': EnvironmentRead.mobileNumber
            }
            response = requests.post(url, data=json.dumps(body), headers=headers)
            print(json.dumps(response.json(), indent=4))
            userKey = response.json()
            sessionKey = response.json()
            print(response.status_code)
            print(response.headers)
            self.assertEqual(202, response.status_code)

        data = {"userKey": userKey['userKey'], "sessionKey": sessionKey['sessionKey']}
        with open('responsedata1.json', "w") as f:
            json.dump(data, f)
