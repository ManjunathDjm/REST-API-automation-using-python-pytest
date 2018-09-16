from unittest import TestCase
import json
import requests
import pytest
import EnvironmentRead


class Feedback(TestCase):
    def setUp(self):
        print("this is Feedback setup")

    def tearDown(self):
        print("this is Feedback teardown")

    @pytest.mark.run(order=13)
    def test_feedback(self):
        with open('responsedata.json') as f:
            applicationId = json.loads(f.read())
            applicationId = applicationId['applicationId']
            print(applicationId)

        url = str(EnvironmentRead.ipPort) + "/v1/users/" + applicationId + "/feedback?access_token={0}".format(
            EnvironmentRead.access_token)

        with open('responsedata.json') as f:
            sessionKey = json.loads(f.read())
            sessionKey = sessionKey['sessionKey']
            print(sessionKey)

        headers = {'Content-type': 'application/json', 'SessionKey': sessionKey}

        body = {
            "reason": "sasa",
            "message": "sasa"

        }

        response = requests.post(url, data=json.dumps(body), headers=headers)
        print(json.dumps(response.json(), indent=4))
        print(response.status_code)
        self.assertEqual(200, response.status_code)
