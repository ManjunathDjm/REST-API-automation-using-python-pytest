from unittest import TestCase
import json
import requests
import pytest
import EnvironmentRead


class RefreshToken(TestCase):

    def setUp(self):
        print("this is RefreshToken setup")

    def tearDown(self):
        print("this is RefreshToken tear down")

    @pytest.mark.run(order=8)
    def test_refreshtoken(self):
        with open('responsedata.json') as f:
            applicationId = json.loads(f.read())
            applicationId = applicationId['applicationId']
            print(applicationId)

        url = str(
            EnvironmentRead.ipPort) + "/v1/users/" + applicationId + "/refreshtoken?access_token={0}".format(
            EnvironmentRead.access_token)

        response = requests.get(url)
        print(json.dumps(response.json(), indent=4))
        print(response.status_code)
        print(response.headers)
        self.assertEqual(200, response.status_code)
