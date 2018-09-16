from unittest import TestCase
import json
import requests
import pytest
import EnvironmentRead


class Search(TestCase):

    def setUp(self):
        print("this is Search setup")

    def tearDown(self):
        print("this is Search tear down")

    @pytest.mark.run(order=16)
    def test_search(self):
        with open('responsedata.json') as f:
            applicationId = json.loads(f.read())
            applicationId = applicationId['applicationId']
            print(applicationId)

            url = str(EnvironmentRead.ipPort) + "/v1/" + applicationId + "/stickers/search?" \
                                                                                 "category=Emotions&keyword=love&access_token={0}".format(
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
