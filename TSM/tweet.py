import twitter
from TSM import app,db

api = twitter.Api(consumer_key='is3JgCTQZcTxC87PsGrI5Q',
                          consumer_secret='VFnHUmfvndxelIpNIaCkpBQqtqeJfFR8tQMW2e0HVK0',
                          access_token_key='741348853-CVJt6XlNS9m8QJtQuHSGyG5GCSXV8TruHvsB1DyH',
                          access_token_secret='kmw4GcUGVEeQKy242k2LTxk5pp7OCkC4elqqMY8VX0')


def Geocode_Search(lat,lng,radius,last_id):
	if last_id is '':
		last_id = 0
		
	results = api.GetSearch(geocode = (lat,lng,radius),since_id=last_id)
	
	last_id = long(max[x.id for x in results])
	
	result_id = []
	result_id.append(results)
	result_id.append(last_id)
	return result_id
	


