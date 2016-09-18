import requests

def get_weather_forecast():

	# Using the api
	url = "http://api.openweathermap.org/data/2.5/weather?q=Orlando,fl&units=imperial&appid=c182e87929dec93e1717d91fe293dd3f"
	weather_request = requests.get(url)
	weather_json = weather_request.json()

	# Forecast description
	description = weather_json['weather'][0]['description']

	# Min-max temperature
	temp_min = weather_json['main']['temp_min']
	temp_max = weather_json['main']['temp_max']

	# Forecast String
	forecast = "Circus forecast for today is "
	forecast += description + " with a high of "
	forecast += str(int(temp_max)) + " and a low of "
	forecast += str(int(temp_min)) + "."

	return forecast