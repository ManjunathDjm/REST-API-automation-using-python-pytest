from unittest import TestCase
import json
import requests
import pytest
import EnvironmentRead


class UserProfileGET(TestCase):
    def setUp(self):
        print("this is userprofileGET setup")

    def tearDown(self):
        print("this is userprofileGEt tear down")

    @pytest.mark.run(order=7)
    def test_UserprofileGET(self):
        with open('responsedata.json') as f:
            applicationId = json.loads(f.read())
            applicationId = applicationId['applicationId']
            print(applicationId)

        url = str(EnvironmentRead.ipPort) + "/v1/users/" + applicationId + "/profile?" \
                                                                                   "channel=Mobile&access_token={0}".format(
            EnvironmentRead.access_token)
        with open('responsedata.json') as f:
            sessionKey = json.loads(f.read())
            sessionKey = sessionKey['sessionKey']
            print(sessionKey)

        with open('responsedata1.json') as f:
            userKey = json.loads(f.read())
            userKey = userKey['userKey']
            print(userKey)

        headers = {'Content-type': 'application/json', 'SessionKey': sessionKey, 'UserKey': userKey}

        response = requests.get(url, data=json.dumps(headers), headers=headers)
        print(json.dumps(response.json(), indent=4))
        print(response.status_code)
        print(response.headers)
        self.assertEqual(200, response.status_code)
