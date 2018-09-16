import unittest
import json
import requests
import EnvironmentRead
import pytest


class ReadOTP(unittest.TestCase):
    def setUp(self):
        print("this is ReadOTP setup")

    def tearDown(self):
        print("this is ReadOTP teardown")

    @pytest.mark.run(order=3)
    def test_ReadOTP(self):
        url = str(
            EnvironmentRead.ipPort) + "/v1/users/readotp?access_token={0}".format(EnvironmentRead.access_token)

        with open('responsedata.json') as f:
            sessionKey = json.loads(f.read())
            sessionKey = sessionKey['sessionKey']
            print(sessionKey)

        headers = {'Content-type': 'application/json', 'SessionKey': sessionKey}

        response = requests.get(url, data=json.dumps(headers), headers=headers)
        print(json.dumps(response.json(), indent=4))
        otp = response.json()
        print(otp)
        print(response.status_code)
        print(response.headers)
        self.assertEqual(200, response.status_code)
        data = {"otp": otp}
        with open('otp.json', "w") as f:
            json.dump(data, f)
