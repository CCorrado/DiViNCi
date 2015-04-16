import rauth
import time
import argparse

DEFAULTTERM = 'Bars'

def main():
    #locations = [(40.734059,-74.029192),(40.748867,-74.038522),(40.758782,-74.022961)]
    locations = [(40.748867,-74.038522)]
    api_calls = []
    section = None
    found = []

    for lat,long in locations:
    	params = get_search_parameters(lat,long)
    	api_calls.append(get_results(params))
    	time.sleep(0.1)

    	for location in api_calls:
            for business in location['businesses']:
	        bizname= []
		bizcag= []
		coordx= []
		coordy= []
		categ= []
		categ_det= []
		loc_detail= []
		coord_detail = []
		bizname = business['name']
		categ = business['categories'] 
		categ_det = categ[0]
		bizcag = categ_det[0]
  	        loc_detail = business['location']
	        coord_detail = loc_detail['coordinate']
	        coordx = coord_detail['latitude']
	        coordy = coord_detail['longitude']
		print (bizname,coordx,coordy,bizcag)

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
    params["limit"] = "1"

    return params

if __name__=="__main__":
    main()
