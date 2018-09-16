from unittest import TestCase
import json
import requests
import pytest
import EnvironmentRead


class ContactUs(TestCase):

    def setUp(self):
        print("this is Contactus setup")

    def tearDown(self):
        print("thios is Contactus teardown")

    @pytest.mark.run(order=14)
    def test_contactus(self):
        with open('responsedata.json') as f:
            applicationId = json.loads(f.read())
            applicationId = applicationId['applicationId']
            print(applicationId)

        url = str(EnvironmentRead.ipPort) + "/v1/users/" + applicationId + "/contactus?access_token={0}".format(
            EnvironmentRead.access_token)

        with open('responsedata.json') as f:
            sessionKey = json.loads(f.read())
            sessionKey = sessionKey['sessionKey']
            print(sessionKey)

        headers = {'Content-type': 'application/json', 'SessionKey': sessionKey}

        body = {

            'name': "sasa",
            'message': 'sasa',
            "emailAddress": 'Raj@gmail.com',
            'purpose': 'sasa'
        }
        response = requests.post(url, data=json.dumps(body), headers=headers)
        print(json.dumps(response.json(), indent=4))
        print(response.status_code)
        self.assertEqual(200, response.status_code)
