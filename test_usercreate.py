import json
import requests
import pytest
from unittest import TestCase
import EnvironmentRead
import uuid


class UserCreate(TestCase):
    def setUp(self):
        print("this is userprofileGET setup")

    def tearDown(self):
        print("this is userprofileGEt tear down")

    @pytest.mark.run(order=1)
    def test_usercreate(self):
        url = str(EnvironmentRead.ipPort) + "/v1/users/create?access_token={0}".format(
            EnvironmentRead.access_token)

        headers = {'Content-type': 'application/json'}

        for i in range(1):
            print(uuid.uuid4())

            filename = "device.json"
            file = open('device.json', "w")
            file.write(str(uuid.uuid4()))
            json.dumps(filename)
            file.close()

            file = open('device.json', "r")
            deviceId = (file.read())
            print(deviceId)

            body = {

                'deviceId': deviceId,
                'notificationId': None,
                'manufacturingDetails': None,
                'advertisementId': None,
                'platform': 'android',
                'deviceToken': deviceId
            }

            data = body
            response = requests.post(url, data=data)
            print(json.dumps(response.json(), indent=4))
            applicationId = response.json()
            sessionKey = response.json()
            print(response.status_code)
            print(response.headers)
            self.assertEqual(response.status_code, 200)

            data = {"applicationId": applicationId['applicationId'], "sessionKey": sessionKey['sessionKey']}
            with open('responsedata.json', "w") as f:
                json.dump(data, f)
