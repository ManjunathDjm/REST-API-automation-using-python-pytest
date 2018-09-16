from unittest import TestCase
import json
import requests
import pytest
import EnvironmentRead


class FBLogin(TestCase):
    def setUp(self):
        print("this is FBLogin setup")

    def tearDown(self):
        print("this is FBLogin teardown")

    @pytest.mark.run(order=10)
    def test_FbLogin(self):
        with open('responsedata.json') as f:
            applicationId = json.loads(f.read())
            applicationId = applicationId['applicationId']
            print(applicationId)

        url = str(
            EnvironmentRead.ipPort) + "/saveyra/v1/users/" + applicationId + "/login?access_token={0}".format(
            EnvironmentRead.access_token)

        with open('responsedata.json') as f:
            sessionKey = json.loads(f.read())
            sessionKey = sessionKey['sessionKey']
            print(sessionKey)

        headers = {'Content-type': 'application/json', 'SessionKey': sessionKey}

        body = {

            'user': '160937508154168',
            'channel': "Fb",
            'token': 'EAAawg1UbqnoBAL3ogZAcpHqe1eTCBYrAx4hsvlBYSgGdizY7BRuD3D9TJzkHu0wPRZApdGe2MKT'
                             }

        response = requests.post(url, data=json.dumps(body), headers=headers)
        print(json.dumps(response.json(), indent=4))
        print(response.status_code)
        self.assertEqual(200, response.status_code)
