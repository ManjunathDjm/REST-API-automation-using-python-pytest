from unittest import TestCase
import json
import requests
import pytest
import EnvironmentRead


class ResendOTP(TestCase):

    def setUp(self):
        print("this is ResendOTP setup")

    def tearDown(self):
        print("this is ResendOTP tear down")

    @pytest.mark.run(order=5)
    def test_Resend_OTP(self):
        with open('responsedata.json') as f:
            applicationId = json.loads(f.read())
            applicationId = applicationId['applicationId']
            print(applicationId)

        url = str(EnvironmentRead.ipPort) + "/v1/users/" + applicationId + "/resendotp?access_token={0}".format(
            EnvironmentRead.access_token)

        with open('responsedata.json') as f:
            sessionKey = json.loads(f.read())
            sessionKey = sessionKey['sessionKey']
            print(sessionKey)

        headers = {'Content-type': 'application/json', 'SessionKey': sessionKey}

        body = {

            'mobileNumber': EnvironmentRead.mobileNumber
        }
        response = requests.post(url, data=json.dumps(body), headers=headers)
        print(json.dumps(response.json(), indent=4))
        print(response.status_code)
        print(response.headers)
        self.assertEqual(200, response.status_code)
