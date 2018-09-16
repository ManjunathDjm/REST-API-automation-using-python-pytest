from unittest import TestCase
import json
import requests
import pytest
import EnvironmentRead


class Configuration(TestCase):

    @pytest.mark.run(order=19)
    def setUp(self):
        print("this is Configuration setup")

    def tearDown(self):
        print("thios is Congiguration teardown")

    @pytest.mark.run(order=19)
    def test_configuration(self):
        with open('responsedata.json') as f:
            applicationId = json.loads(f.read())
            applicationId = applicationId['applicationId']
            print(applicationId)

        url = str(
            EnvironmentRead.ipPort) + "/v1/" + applicationId + "/application/configurations?access_token={0}".format(
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
        self.assertEqual(response.status_code, 200)
