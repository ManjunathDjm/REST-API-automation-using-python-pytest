from unittest import TestCase
import json
import requests
import pytest
import EnvironmentRead


class Registration(TestCase):

    def setUp(self):
        print("this is Registration setup")

    def tearDown(self):
        print("this is Regidtration tear down")

    @pytest.mark.run(order=2)
    def test2_Registration(self):
        url = str(
            EnvironmentRead.ipPort) + "/v1/users/register?access_token={0}".format(EnvironmentRead.access_token)

        with open('responsedata.json') as f:
            sessionKey = json.loads(f.read())
            sessionKey = sessionKey['sessionKey']
            print(sessionKey)

        headers = {'Content-type': 'application/json', 'SessionKey': sessionKey}

        with open('responsedata.json') as f:
            applicationId = json.loads(f.read())
            applicationId = applicationId['applicationId']
            print(applicationId)

        body = {

            'applicationId': applicationId,
            'channel': 'Mobile',
            'mobileNumber': EnvironmentRead.mobileNumber,
            'facebookId': None,
            'token': None

        }

        response = requests.post(url, data=json.dumps(body), headers=headers)
        print(json.dumps(response.json(), indent=4))
        print(response.status_code)
        self.assertEqual(200, response.status_code)
