import rauth
import time
import argparse

DEFAULTTERM = 'Bars'

def main():
    locations = [(40.734059,-74.029192),(40.748867,-74.038522),(40.758782,-74.022961)]
    api_calls = []
    section = None
    found = []

    for lat,long in locations:
        params = get_search_parameters(lat,long)
        api_calls.append(get_results(params))
        time.sleep(0.5)

    for location in api_calls:
        for business in location['businesses']:
	    print business['name'], business['location']
	    loc_detail = []
  	    loc_detail = business['location']
	    #for line in loc_detail:
		#left,sep,right = line.partition('coordinate')
		#if sep:
		#print(line)

def get_results(params):

    #Obtain these from Yelp's manage access page
    consumer_key = 'pcF2y7MTUrLwT35gmzXqnA'
    consumer_secret = 'FCuLVFtyrzU4HhVmxvBt8ATTDvQ'
    token = 'M9OLuNKO2W4bKG9iDwl3cTZK0vC6yrMb'
    token_secret = 'cnicukO-oeJ_phWy1LrHsBaAWfE'

    session = rauth.OAuth1Session(
        consumer_key = consumer_key
        ,consumer_secret = consumer_secret
        ,access_token = token
        ,access_token_secret = token_secret)

    request = session.get("http://api.yelp.com/v2/search",params=params)

    #Transforms the JSON API response into a Python dictionary
    data = request.json()
    session.close()

    return data

def get_search_parameters(lat,long):
    #See the Yelp API for more details
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--term', dest='term', default=DEFAULTTERM, type=str, help='Search term (default: %(default)s)')
    #parser.add_argument('-l', '--location', dest='locations', type=str, help='Search location (default: %(default)s)')
    input_values = parser.parse_args()

    params = {}
    params["term"] = input_values.term
    params["ll"] = "{},{}".format(str(lat),str(long))
    params["radius_filter"] = "2000"
    params["limit"] = "20"

    return params

if __name__=="__main__":
    main()
