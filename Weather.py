
from pyowm import OWM
from twilio.rest import TwilioRestClient
import json

#CONSTANTS VARIABLES
TWILIO_ACCOUNT_SID = "YOUR SID"
TWILIO_AUTH_TOKEN = "YOUR AUTH TOKEN"
FROM_NUMBER = "YOUR TWILIO NUMBER"
TO_NUMBER = "YOUR NUMBER"
PYOWMM_API_KEY = "YOUR PYOWM KEY"

CLIENT = TwilioRestClient(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
owm = OWM(PYOWM_API_KEY)


def sendMessage():
	#Obtain the weather instance
	weather_data = owm.weather_at_place("Toronto,ca")#You can change the place as per your requirements
	the_weather = weather_data.get_weather()

	#Query for specific data
	forecast = str(the_weather.get_detailed_status())
	#Data stored in json in dictionary format. This allows for easy access to individual elements
	temperature_json = the_weather.get_temperature('celsius')
	temperature = "%s" % temperature_json["temp"]

	#send message to device through twilio
	message = CLIENT.messages.create(to = TO_NUMBER, from_ = FROM_NUMBER, body = "There's" +" "+ forecast +" "+ "with a temparature of" 
		+ " " + temperature +" "+ "degrees celsius"+" "+"today" )
	return message	


if __name__ == "__main__":

	sendMessage()
	
