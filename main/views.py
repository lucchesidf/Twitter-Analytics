from django.shortcuts import render
from django.http import HttpResponse
from geopy.geocoders import Nominatim

import json
import oauth2

def index(request):

		geolocator = Nominatim()
		geolocator=Nominatim(timeout=10)
		location = geolocator.geocode("Brasília Distrito Federal")
		variable_address = location.address
		variable_latitude = location.latitude
		variable_longitude = location.longitude
		latitude_str =  str(variable_latitude)
		longitude_str = str(variable_longitude)

		consumer_key = 'OfMKxNKdAm6FBHCIUZeV2cp3V'
		consumer_secret = '5M4ZyY8xrA3eVaPVNbZ5pFuheaiUTRCpd1Y5VNR8oWhQL6KcYW'

		access_token = '2727885369-3s8i9LPX5GdUxP9UUDKyLcl9cPps7Gf31DzkYmE'
		token_secret = 'Fzsas4jU5Q4qFEfRUGmmuXrIIEBHBROYm1fB40csZCC67'

		consumer = oauth2.Consumer(consumer_key, consumer_secret)
		token = oauth2.Token(access_token, token_secret)
		cliente = oauth2.Client(consumer, token)

		requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?geocode=' + latitude_str +',' + longitude_str + ',1km' + '&count=100')
		#geocode=37.781157,-122.398720,20km

		decodificar = requisicao[1].decode()

		objeto = json.loads(decodificar)

		variables = {

			'address': variable_address,
			'latitude': variable_latitude,
			'longitude': variable_longitude,
			'tweets': objeto['statuses']
		}

		return render(request, 'index.html', variables)
