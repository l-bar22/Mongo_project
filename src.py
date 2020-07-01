def getAirportFoursquare():

    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        Client_Id=os.getenv("clientID"),
        Client_Secret=os.getenv("clientSecret"),
        ll='1.352083,103.819836',
        
        
    )
    resp = requests.get(url=url, params=params)

    data = json.loads(resp.text)


def getStadiumFoursquare():

    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        Client_Id=os.getenv("clientID"),
        Client_Secret=os.getenv("clientSecret"),
        ll='1.352083,103.819836',
        query="stadium",
        
    )
    resp = requests.get(url=url, params=params)

    data = json.loads(resp.text)

def getStarbucksFoursquare():

    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        Client_Id=os.getenv("clientID"),
        Client_Secret=os.getenv("clientSecret"),
        ll='1.352083,103.819836',
        query="Starbucks",
        limit=1000,
    )
    resp = requests.get(url=url, params=params)

    data = json.loads(resp.text)


def getSchoolFoursquare():

    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        Client_Id=os.getenv("clientID"),
        Client_Secret=os.getenv("clientSecret"),
        ll='1.352083,103.819836',
        query="School",
        limit=1000,
    )
    resp = requests.get(url=url, params=params)

    data = json.loads(resp.text)


def getVeganFoursquare():

    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        Client_Id=os.getenv("clientID"),
        Client_Secret=os.getenv("clientSecret"),
        ll='1.352083,103.819836',
        query="vegan",
        limit=1000,
    )
    resp = requests.get(url=url, params=params)

    data = json.loads(resp.text)


def getDogGroomerFoursquare():

    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        Client_Id=os.getenv("clientID"),
        Client_Secret=os.getenv("clientSecret"),
        ll='1.352083,103.819836',
        query="doggroomer",
        limit=1000,
    )
    resp = requests.get(url=url, params=params)

    data = json.loads(resp.text)


def getPubsFoursquare():

    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        Client_Id=os.getenv("clientID"),
        Client_Secret=os.getenv("clientSecret"),
        ll='1.352083,103.819836',
        query="pubs",
        limit=1000,
    )
    resp = requests.get(url=url, params=params)

    data = json.loads(resp.text)