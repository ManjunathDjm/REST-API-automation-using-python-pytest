from unittest import TestCase
import json
import requests
import pytest
import EnvironmentRead


class UserProfilePUT(TestCase):

    def setUp(self):
        print("this is UserProfilePUT setup")

    def tearDown(self):
        print("this is UserprofilePut tear down")

    @pytest.mark.run(order=6)
    def test_Userprofile_PUT(self):
        with open('responsedata.json') as f:
            applicationId = json.loads(f.read())
            applicationId = applicationId['applicationId']
            print(applicationId)

            url = str(EnvironmentRead.ipPort) + "/v1/users/" + applicationId + "/profile?" \
                                                                                       "channel=Mobile&access_token={0}".format(
                EnvironmentRead.access_token)
            with open('responsedata1.json') as f:
                userKey = json.loads(f.read())
                userKey = userKey['userKey']
                print(userKey)

            with open('responsedata.json') as f:
                sessionKey = json.loads(f.read())
                sessionKey = sessionKey['sessionKey']
                print(sessionKey)

            headers = {'Content-type': 'application/json', 'SessionKey': sessionKey, 'UserKey': userKey}

            body = {

                "education": EnvironmentRead.education,
                "channel": EnvironmentRead.channel,
                "email": EnvironmentRead.email,
                "mobileNumber": EnvironmentRead.mobileNumber,
                "name": "",
                "language": "",
                "gender": ""
            }

            response = requests.put(url, data=json.dumps(body), headers=headers)
            print(json.dumps(response.json(), indent=4))
            print(response.status_code)
            print(response.headers)
