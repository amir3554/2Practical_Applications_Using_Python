import requests, json




# Section 3
api_key = '...'''#amir's
api_key2= '...'''#Default
api_key3= '...'''# Amir's


# Section 1
base_url = 'https://api.openweathermap.org/data/2.5/weather?'


# Section 2
city_name = input("Enter The city name: ")


# Complete url address
complete_url = f"{base_url}q={city_name}&units=metric&appid={api_key}"
print(complete_url)


#Response object
response = requests.get(complete_url)


x = json.loads(response.text)
if x["cod"] != "404":

    y = x['main']
    current_temprature = y["temp"]
    current_humidity = y["humidity"]
    current_pressure = y["pressure"]
    z = x['weather']
    weather_description = z[0]["description"]

    print(f"The temprature (in metric) is :{str(current_temprature)} Cº, \nThe pressure (in metric) is :{str(current_pressure)}, \nHumidity (in metric) is :{current_humidity}, \nThe Description of the weather is :{weather_description}.")

else:
    print("city Not found.")


