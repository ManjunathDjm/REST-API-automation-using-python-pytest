from unittest import TestCase
import json
import requests
import pytest
import EnvironmentRead


class NotificationPreferencesPUT(TestCase):

    def setUp(self):
        print("this is NotificationpreferancePUT setup")

    def tearDown(self):
        print("this is NotificationpreferancePUT teardown")

    @pytest.mark.run(order=11)
    def test_notificationpreferencesPUT(self):
        with open('responsedata.json') as f:
            applicationId = json.loads(f.read())
            applicationId = applicationId['applicationId']
            print(applicationId)

            url = str(
                EnvironmentRead.ipPort) + "/v1/users/" + applicationId + "/preferences?access_token={0}".format(
                EnvironmentRead.access_token)

            with open('responsedata.json') as f:
                sessionKey = json.loads(f.read())
                sessionKey = sessionKey['sessionKey']
                print(sessionKey)

            headers = {'Content-type': 'application/json', 'SessionKey': sessionKey}

            body = {

                'contentType': '',
                'applicationId': applicationId,
                'frequency': '',
                'status': 'false',
                'ringtone': 'fsss'

            }

            response = requests.put(url, data=json.dumps(headers), headers=headers)
            print(json.dumps(response.json(), indent=4))
            print(response.status_code)
            print(response.headers)
            self.assertEqual(200, response.status_code)
