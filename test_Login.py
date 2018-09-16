from unittest import TestCase
import json
import requests
import pytest
import EnvironmentRead


class Login(TestCase):

    def setUp(self):
        print("this is Login setup")

    def tearDown(self):
        print("this is Login teardown")

    @pytest.mark.run(order=9)
    def test_login(self):
        with open('responsedata.json') as f:
            applicationId = json.loads(f.read())
            applicationId = applicationId['applicationId']
            print(applicationId)

            url = str(
                EnvironmentRead.ipPort) + "/v1/users/" + applicationId + "/login?access_token={0}".format(
                EnvironmentRead.access_token)
            headers = {'Content-type': 'application/json'}

            body = {
                'user': EnvironmentRead.mobileNumber,
                'channel': 'Mobile'
            }

            response = requests.post(url, data=json.dumps(body), headers=headers, verify=False)
            print(json.dumps(response.json(), indent=4))
            print(response.status_code)
            self.assertEqual(200, response.status_code)
