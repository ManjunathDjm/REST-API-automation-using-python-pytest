from unittest import TestCase
import json
import requests
import pytest
import EnvironmentRead


class KeyboardHomeScreen(TestCase):

    def setUp(self):
        print("this is KeyboardHomescreen setup")

    def tearDown(self):
        print("this is KeyboardHomescreen teardown")

    @pytest.mark.run(order=15)
    def test_keyboardhomescreen(self):
        with open('responsedata.json') as f:
            applicationId = json.loads(f.read())
            applicationId = applicationId['applicationId']
            print(applicationId)

            url = str(
                EnvironmentRead.ipPort) + "/v1/" + applicationId + "/stickers/keyboard/homescreen?access_token={0}".format(
                EnvironmentRead.access_token)

            with open('responsedata.json') as f:
                sessionKey = json.loads(f.read())
                sessionKey = sessionKey['sessionKey']
                print(sessionKey)

            headers = {'Content-type': 'application/json', 'SessionKey': sessionKey}

            response = requests.get(url, data=json.dumps(headers), headers=headers)
            print(json.dumps(response.json(), indent=4))
            print(response.status_code)
            print(response.headers)
            self.assertEqual(200, response.status_code)
