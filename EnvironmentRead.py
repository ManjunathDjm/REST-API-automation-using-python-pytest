from configparser import ConfigParser

# change the environment name according to Environment.ini
parser = ConfigParser()
parser.read('Environment.ini')
ipPort = parser.get('instance', 'dev')
print(parser.get('instance', 'dev'))

################################################
# VALID DATA
# ACCESS TOKEN -No need to change any data
access_token = parser.get('access_token', 'access_token')
print(parser.get('access_token', 'access_token'))

# MOBILE NUMBER No need to change data
mobileNumber = parser.get('mobileNumber', 'mobileNumber')
print(parser.get('mobileNumber', 'mobileNumber'))

# EDUCATION no need to change data
education = parser.get('education', 'education')
print(parser.get('education', 'education'))

# CHANNEL No need to change data
channel = parser.get('channel', 'channel')
print(parser.get('channel', 'channel'))

# CHANNEL No need to change data
email = parser.get('email', 'email')
print(parser.get('email', 'email'))

# CHANNEL No need to change data
name = parser.get('name', 'name')
print(parser.get('name', 'name'))

# LANGUAGE No need to change data
language = parser.get('language', 'language')
print(parser.get('language', 'language'))

# CHANNEL No need to change data
gender = parser.get('gender', 'gender')
print(parser.get('gender', 'gender'))


####################################################

# INVALID DATA
# ACCESS TOKEN -No need to change any data
access_token_invalid = parser.get('access_token_invalid', 'access_token_invalid')
print(parser.get('access_token_invalid', 'access_token_invalid'))

# MOBILE NUMBER No need to change data
mobileNumber_invalid = parser.get('mobileNumber_invalid', 'mobileNumber_invalid')
print(parser.get('mobileNumber_invalid', 'mobileNumber_invalid'))

# EDUCATION no need to change data
education_invalid = parser.get('education_invalid', 'education_invalid')
print(parser.get('education_invalid', 'education_invalid'))

# CHANNEL No need to change data
channel_invalid = parser.get('channel_invalid', 'channel_invalid')
print(parser.get('channel_invalid', 'channel_invalid'))

# CHANNEL No need to change data
email_invalid = parser.get('email_invalid', 'email_invalid')
print(parser.get('email', 'email'))

# CHANNEL No need to change data
name_invalid = parser.get('name_invalid', 'name_invalid')
print(parser.get('name_invalid', 'name_invalid'))

# LANGUAGE No need to change data
language_invalid = parser.get('language_invalid', 'language_invalid')
print(parser.get('language_invalid', 'language_invalid'))

# CHANNEL No need to change data
gender_invalid = parser.get('gender_invalid', 'gender_invalid')
print(parser.get('gender_invalid', 'gender_invalid'))



