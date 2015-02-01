import urllib
import base64
import requests
import json
import uuid

TWITTER_API_KEY=""
TWITTER_API_SECRET=""

BEARER_TOKEN_CREDENTIALS="%s:%s" % (urllib.quote(TWITTER_API_KEY),
				    urllib.quote(TWITTER_API_SECRET))
BEARER_TOKEN = base64.b64encode(BEARER_TOKEN_CREDENTIALS)

TOKEN_URL="https://api.twitter.com/oauth2/token"
token_headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                 'Authorization': "Basic " + BEARER_TOKEN}
body="grant_type=client_credentials"

token_req = requests.post(TOKEN_URL, headers=token_headers, data=body)
j = json.loads(token_req.text)
ACCESS_TOKEN = j['access_token']
content_headers = {'Authorization': "Bearer " + ACCESS_TOKEN}

print content_headers

OTTAWA_LAT=45.4214
OTTAWA_LON=-75.6919
HALIFAX_LAT=44.6478
HALIFAX_LON=-63.5714
GANDER_LAT=48.9569
GANDER_LON=-54.6089
CHARLOTTETOWN_LAT=46.2400
CHARLOTTETOWN_LON=-63.1399
FREDERICTON_LAT=45.9500
FREDERICTON_LON=-66.6667
MONCTON_LAT=-46.1328
MONCTON_LON=-64.7714
STJOHN_LAT=45.2796
STJOHN_LON=-66.0628
STJOHNS_LAT=47.5675
STJOHNS_LON=-52.7072
CONTENT_URL="https://api.twitter.com/1.1/search/tweets.json?q={q}&geocode={lat},{lon},{radius}&result_type=recent"

def twittersearch(lat=OTTAWA_LAT, lon=OTTAWA_LON, q="snow", radius="10km"):
    q = "" if not q else q
    instantiated = CONTENT_URL.format(q=q, lat=lat, lon=lon, radius=radius)
    # instantiated = CONTENT_URL
    print instantiated
    path = str(uuid.uuid4()) + ".json"
    content_req = requests.get(instantiated, headers=content_headers)
    print content_req
    with open(path, 'w') as f:
        print >> f, json.dumps(content_req.json(),
                               sort_keys=True,
                               indent=4)

twittersearch(q="", lat=HALIFAX_LAT, lon=HALIFAX_LON)
twittersearch(q="", lat=GANDER_LAT, lon=GANDER_LON)
twittersearch(q="", lat=CHARLOTTETOWN_LAT, lon=CHARLOTTETOWN_LON)
twittersearch(q="", lat=FREDERICTON_LAT, lon=FREDERICTON_LON)
twittersearch(q="", lat=MONCTON_LAT, lon=MONCTON_LON)
twittersearch(q="", lat=STJOHN_LAT, lon=STJOHN_LON)
twittersearch(q="", lat=STJOHNS_LAT, lon=STJOHNS_LON)
