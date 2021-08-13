import unittest
import requests
from main import app
from distance.get_distance import get_distance_with_geocoder

destination = 'Kazan'

#Function converts a list into a string
def listToString(s):
	str1 = " "  
	return (str1.join(s))

class DistanceTestCase(unittest.TestCase):	

	def test_1_index(self):
		tester = app.test_client(self)
		res = tester.get('/distance', content_type='html/text')
		self.assertEqual(res.status_code, 200)


	#Test's the yandex api to get the 1st location (MKAD Moscow, Russian Federation)
	def test_2_location1(self):
		location1 = requests.get('https://geocode-maps.yandex.ru/1.x/?apikey=71f8265c-edd8-40e2-be92-8ad9fb6edc1e&geocode=MKAD+Moscow,Russian+Federation&lang=en_US&format=json')
		res = location1
		self.assertTrue(res.status_code, 200)

	#Test's for the destination
	def test_3_location2(self):
		location2 = requests.get('https://geocode-maps.yandex.ru/1.x/?apikey=71f8265c-edd8-40e2-be92-8ad9fb6edc1e&geocode='+listToString(destination.replace(' ','+').split(',')[::-1])+'&lang=en_US&format=json')
		res = location2
		self.assertTrue(res.status_code, 200)

	#Test's the function get_distance_with_geocoder
	def test_4_get_distance(self):
		distance = get_distance_with_geocoder(destination)
		res = distance
		self.assertTrue(res, 200)

	#Test's for correct input
	def test_5_correct_input(self):
		tester = app.test_client(self)
		res = tester.post(destination)
		self.assertTrue(res.status_code, 201)

	#Test's for incorrect input
	def test_6_incorrect_input(self):
		destination=' '
		tester = app.test_client(self)
		res = tester.post(destination)
		self.assertEqual(res.status_code, 404)


if __name__ == '__main__':
	unittest.main()