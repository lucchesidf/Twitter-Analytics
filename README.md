How it works?

the whole joke happens inside views.py specifically inside the index () function

first we set a TimeOut of 10 seconds to not occur a TimeOut error by the Nominatim,
then we collect data from the current location as address, lat and long, and assign the variables
variable_address, variable_latitude and variable_longitude, then convert them to string.

Now comes the part of the authentication in the api of Twitter, you need to go to the developer page and get your keys, since I will not make my own :p

Replace the values of the following variables with your twitter api credentials:

consumer_key
consumer_secret
access_token
token_secret

The API we'll be using is this (https://api.twitter.com/1.1/search/tweets.json)

we will use some arguments within this api

?geocode = #Here we insert our latitude, longitude and radius in km in the following format ?geocode=-15,7942287,-47,8821658,1km

&count = # Here we insert how many tweets we want the api to return, the maximum is 100 so we will put 100

After that we organize all the information we need in variables and go to our html page using the return render according to line 44 of views.py

How to run:

python manage.py runserver

Access: http://localhost:8000


Feel free to collaborate with something :)



Developed by Gabriel Lucchesi.
