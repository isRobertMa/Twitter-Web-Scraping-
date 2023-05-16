"""
This is a testing file, this is a direct copy of github repository 'Twitter_API_V2-sample-code/User-Lookup'.
This file serves as testing ground for understanding OAuth1 and basic twitter Functions from twitter API.
Since previous attemps at postman and home build tweepy results in Error 403 authetication error, direct
copy of sample code will speed up the learning process.  
"""
from requests_oauthlib import OAuth1Session
import os
import json
import pandas as pd
import requests

# In your terminal please set your environment variables by running the following lines of code.
# export 'CONSUMER_KEY'='<9G7CGyyHZiwqTXLfh9HsMIcuQ>'
# export 'CONSUMER_SECRET'='<GNt3PsbCCyFy5inYujkaxs0o6Tf4BONtDvH7mJNbB8gHHuixCb>'

consumer_key = '9G7CGyyHZiwqTXLfh9HsMIcuQ'
consumer_secret = 'GNt3PsbCCyFy5inYujkaxs0o6Tf4BONtDvH7mJNbB8gHHuixCb'

# User fields are adjustable, options include:
# created_at, description, entities, id, location, name,
# pinned_tweet_id, profile_image_url, protected,
# public_metrics, url, username, verified, and withheld
fields = "created_at,id,name,pinned_tweet_id,username"
params = {"user.fields": fields}

# Get request token, need to change up the request token to include obb so the PIN will be visiable. 
request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

# Catch the potential erros wiht OAu1 tokens
try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError:
    print(
        "There may have been an issue with the consumer_key or consumer_secret you entered."
    )

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)

# # Get authorization
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

# Get the access token
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]

# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

# Returned response field 
response = oauth.get("https://api.twitter.com/2/users/me", params=params)

if response.status_code != 200:
    raise Exception(
        "Request returned an error: {} {}".format(response.status_code, response.text)
    )

print("Response code: {}".format(response.status_code))

json_response = response.json()

print(json.dumps(json_response, indent=4, sort_keys=True))


# The following code will do a seperate data extraction with bearer token
# Set up bearer token credentials 
os.environ["BEARER_TOKEN"] = "AAAAAAAAAAAAAAAAAAAAAPoSngEAAAAAZ6XTXf%2FVHu1%2Bu%2BLDSLaaVYxZ5fI%3DPsfoAw87FDsy6dCZQOEYUTwU2zzywn25iN6Sfup4maM6YXdDVq"
bearer_token = os.environ.get('BEARER_TOKEN')
headers = {"Authorization": "Bearer {}".format(bearer_token)}
# make request to endpoint using request package
url = "https://api.twitter.com/2/tweets/search/recent?query=from:TwitterDev"
response = requests.request("GET", url, headers=headers).json()
print(response)
# create csv file
df = pd.DataFrame(response['data'])
df.to_csv('response_python.csv')