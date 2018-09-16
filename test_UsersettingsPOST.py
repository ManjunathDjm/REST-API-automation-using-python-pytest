from unittest import TestCase
import json
import requests
import pytest
import EnvironmentRead


class UserSettingsPOST(TestCase):

    def setUp(self):
        print("this is UsersettingsPOST setup")

    def tearDown(self):
        print("this is UsersettingsPOST tear down")

    @pytest.mark.run(order=20)
    def test_Usersettings_POST(self):
        with open('responsedata.json') as f:
            applicationId = json.loads(f.read())
            applicationId = applicationId['applicationId']
            print(applicationId)

        url = str(EnvironmentRead.ipPort) + "/v1/users/" + applicationId + "/settings?access_token={0}".format(
            EnvironmentRead.access_token)

        with open('responsedata.json') as f:
            sessionKey = json.loads(f.read())
            sessionKey = sessionKey['sessionKey']
            print(sessionKey)

            headers = {'Content-type': 'application/json', 'Sessionkey': sessionKey}

            response = requests.post(url, data=json.dumps(headers), headers=headers)
            print(json.dumps(response.json(), indent=4))
            print(response.status_code)
            print(response.headers)
            self.assertEqual(200, response.status_code)
