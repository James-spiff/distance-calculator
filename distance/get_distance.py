import requests
import json
import datetime
import logging
import math

logs = logging.getLogger('app_logs')

#This function creates the logs and stores them in a file called results.log
def make_logs():
	handler = logging.FileHandler(r'results.log'.format(datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S_%f')))
	#sets the results from the logs to be stored in the results.log file and indicates the time it was logged 
	handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
	#The formatter converts log records to strings
	logs.addHandler(handler)
	logs.setLevel(10)  #logger.setLevel(logging.DEBUG)
	#Sets the log level at 10 which is the debug level


#Function to calculate the distance between the 2 geolocation points in km
def get_distance(p1, p2):
	logs.info('Distance between 2 points')
	# approximate radius of earth in km
	R = 6373.0

	p1['lat'] = float(p1['lat'])
	p1['long'] = float(p1['long'])
	p2['lat'] = float(p2['lat'])
	p2['long'] = float(p2['long'])

	dlong = math.radians(p2['long'] - p1['long'])
	dlat = math.radians(p2['lat'] - p1['lat'])

	a = math.sin(dlat / 2)**2 + math.cos(p1['lat']) * math.cos(p2['lat']) * math.sin(dlong / 2)**2
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

	distance = R * c
	logs.info('returns the distance in Kilometers')
	return distance

#Function converts a list into a string
def listToString(s):
	str1 = " "  
	return (str1.join(s))


#Function to get the distance using the yandex Geocoder Api
def get_distance_with_geocoder(destination):
	make_logs() #The function that creates our logs
	try:
		logs.info('Initial location: MKAD Moscow, Russian Federation')
		location1 = requests.get('https://geocode-maps.yandex.ru/1.x/?apikey=71f8265c-edd8-40e2-be92-8ad9fb6edc1e&geocode=MKAD+Moscow,Russian+Federation&lang=en_US&format=json') #url + apikey + geocode

		logs.info('Input destination')
		location2 = requests.get('https://geocode-maps.yandex.ru/1.x/?apikey=71f8265c-edd8-40e2-be92-8ad9fb6edc1e&geocode='+listToString(destination.replace(' ','+').split(',')[::-1])+'&lang=en_US&format=json')
		#Gets the location by appending the input string(destination) to the url in the format the api uses
		destination_string = listToString(destination)
		logs.info('If destination is located in Moscow')
		if 'Moscow' in destination:
			return 'Destination is too close try another address'
		else:
			logs.info('Initial location point')
			json_loads = json.loads(location1.text)
			#takes the initial location and converts it to a json object
			p1_lat = json_loads['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')[0]
			p1_long = json_loads['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')[1]

			logs.info('Destination location point')
			json_loads = json.loads(location2.text)
			p2_lat = json_loads['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')[0]
			p2_long = json_loads['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')[1]

			point_one={'lat': p1_lat, 'long': p1_long}
			point_two={'lat': p2_lat, 'long': p2_long}

			logs.info('Point of the first location is :(' + point_one['lat'] + ' , '+ point_one['long'] + ')')
			logs.info('Point of the second location is :(' + point_two['lat'] + ' , '+ point_two['long'] + ')')
			logs.info('The distance between  two location is '+ str(get_distance(point_one, point_two)) + " Km")
	except Exception as e:
			logs.error(e)
			print(e)
			return "Input valid location"
	return "The distance to "+ destination + " is: " + str(round(get_distance(point_one, point_two), 3)) + " Km"

