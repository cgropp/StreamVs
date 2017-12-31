import urllib
from urllib.request import urlopen
from urllib.request import Request
import json
import os
import time

#Loop until valid URL is accepted
validURL = False
while (validURL == False):
	print("Please enter the event name (text after tournament/ in url without /)")
	inputName = input("Ex: https://smash.gg/tournament/triton-smash-sundays-35/ = triton-smash-sundays-35 \n" )
	apiURL = "https://api.smash.gg/tournament/" + inputName

	#Open URL to make API call
	#tournamentJSON = urlopen("https://api.smash.gg/tournament/falcon-punch-fridays-46")

	#Request to see if URL exists
	try:
		request = Request(apiURL)
		handle = urlopen(request)

	except urllib.error.HTTPError as error:
		print ("Error occurred: - %s" % error.code)
		
		#Check for 404 error (Page doesn't exist)
		if error.code == 404:
			print ("Event page does not exist, please try again and make sure you are putting in the proper name")
			
		else:
			print("Non 404 error occurred.")
	#If URL is valid, exit loop		
	else:
		validURL = True


#URL is accepted, get JSON file
tournamentJSON = urlopen(apiURL)


#Load JSON file into variable
tournamentData = json.load(tournamentJSON)
tournamentJSON.close()

#Obtain tournament ID and name
try:
	tournamentID = tournamentData["entities"]["tournament"]["id"]
except KeyError:
	print("ERROR: Tournament ID does not exist, terminating script")
	quit()

try:
	tournamentName = str(tournamentData["entities"]["tournament"]["name"])
except KeyError:
	print("ERROR: Tournament name does not exist")
	tournamentName = "No name found"
	


tournamentID = tournamentData["entities"]["tournament"]["id"]
tournamentName = str(tournamentData["entities"]["tournament"]["name"])


#Construct URL of stream queue api call and open
streamURL = "https://api.smash.gg/station_queue/" + str(tournamentID)

#Check for valid URL
try:
	request = Request(streamURL)
	handle = urlopen(request)

except urllib.error.HTTPError as error:
	print ("Error occurred: - %s" % error.code)
	
	#Check for 404 error (Page doesn't exist)
	if error.code == 404:
		print ("ERROR: Something went wrong, stream queue page does not exist")
		
	else:
		print("Non 404 error occurred.")
		
		
#else: 
	#streamJSON = urlopen(streamURL)
	#Commented out because I will put urlopen call in 30s loop below


#For testing purposes, read local file for JSON
#with open('FPF-Stream-Queue-Ex-poyovsrvr.json', 'r') as f:
#	streamData = json.load(f)
#f.close()

#Loop everything below every 20 seconds:
def streamLoop():
	print("\nNow performing a new stream update cycle.")
	streamJSON = urlopen(streamURL)
	streamData = json.load(streamJSON) 
	streamJSON.close()


	try:
		checkStream = streamData["data"]["entities"]["sets"][0]
	except TypeError:
		print("ERROR: No stream set for this event, terminating script")
		quit()
		#TODO: Potentially make it not even check for other data if this is not found
	except KeyError:
		print("No set currently in stream queue, updating to generic tags/values")
		#TODO: Potentially make it not even check for other data if this is not found

		
	#Extract data about players on stream, if stream queue is up
	try:
		tournamentRound = str(streamData["data"]["entities"]["sets"][0]["midRoundText"])
	except KeyError:
		tournamentRound = "No stream queue"
		
	#tournamentRound = "Fix later"
	try:
		gamerTag1 = str(streamData["data"]["entities"]["player"][0]["gamerTag"])
	except KeyError:
		gamerTag1 = "Player 1"
		
	#TODO: Going to try to use optString
	try:
		twitter1 = str(streamData["data"]["entities"]["player"][0]["twitterHandle"])
	except KeyError:
		twitter1 = "Player 1"

	try:	
		gamerTag2 = str(streamData["data"]["entities"]["player"][1]["gamerTag"])
	except KeyError:
		gamerTag2 = "Player 2"

	try:
		twitter2 = str(streamData["data"]["entities"]["player"][1]["twitterHandle"])
	except KeyError:
		twitter2 = "Player 2 Twitter"

	#Print relevant information
	print("Event name: " + tournamentName)
	print("Stage of tournament on stream: " + tournamentRound)

	print("Player 1 name: " + gamerTag1)
	print("Player 1 twitter handle:  " + twitter1)

	print("Player 2 name: " + gamerTag2)
	print("Player 2 twitter handle:  " + twitter2)

	#Write data to files
	print("Writing data to files")

	#Check if data folder exists
	if not os.path.exists("data"):
		os.makedirs("data")

	tournamentNameFile = open("data/tournamentName.txt","w") 
	tournamentNameFile.write(tournamentName)
	tournamentNameFile.close()

	tournamentRoundFile = open("data/tournamentRound.txt","w") 
	tournamentRoundFile.write(tournamentRound)
	tournamentRoundFile.close()

	gamerTag1File = open("data/gamerTag1.txt","w") 
	gamerTag1File.write(gamerTag1)
	gamerTag1File.close()

	twitter1File = open("data/twitter1.txt","w") 
	twitter1File.write(twitter1)
	twitter1File.close()

	gamerTag2File = open("data/gamerTag2.txt","w") 
	gamerTag2File.write(gamerTag2)
	gamerTag2File.close()

	twitter2File = open("data/twitter2.txt","w") 
	twitter2File.write(twitter2)
	twitter2File.close()

	print("Done writing to files.")
	print("Waiting 20 seconds until next stream loop")
	time.sleep(20)

while True:
	streamLoop();

