from unittest import TestCase
import json
import requests
import EnvironmentRead
import pytest


class FBRegister(TestCase):

    def setUp(self):
        print("this is Facebook registration setup")

    def tearDown(self):
        print("thios is Facebook registration teardown")

    @pytest.mark.run(order=20)
    def test_FbRegistration(self):
        url = str(
            EnvironmentRead.ipPort) + "/saveyra/v1/users/registr?access_token={0}".format(EnvironmentRead.access_token)

        with open('responsedata.json') as f:
            sessionKey = json.loads(f.read())
            sessionKey = sessionKey['sessionKey']
            print(sessionKey)

        with open('responsedata1.json') as f:
            userKey = json.loads(f.read())
            userKey = userKey['userKey']
            print(userKey)

        headers = {'Content-type': 'application/json', 'SessionKey': sessionKey, 'userKey': userKey}

        with open('responsedata.json') as f:
            applicationId = json.loads(f.read())
            applicationId = applicationId['applicationId']
            print(applicationId)

        body = {

            'applicationId': applicationId,
            'channel': 'Fb',
            'mobileNumber': None,
            'facebookId': '175092446687192',
            'token': 'EAAawg1UbqnoBAKrc0fMWcwO9msLatBs1p0vn4nbWTHuCpq02Jyje7NpqiA6fZA3PO4hZBNpe6PBq9r6gVmGW5YnTpeIx6r6WVhwjy'
                     'VRZAZAKYDPAjZAD9wBL0wlGeZAUU9rTFblzW3o13e1Yjq4o8iKwHxAdHerisMnbT6rRWsngZDZD'
        }

        response = requests.post(url, data=json.dumps(body), headers=headers, )
        print(json.dumps(response.json(), indent=4))
        # json.loads(response.content)
        print(response.status_code)
        self.assertEqual(200, response.status_code)
