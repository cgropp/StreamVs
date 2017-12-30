from urllib.request import urlopen
import json
import os

#inputName = input("Please enter the event name (text after smash.gg in url without /) \n" )
#apiURL = "https://api.smash.gg/tournament/" + inputName
#Open URL to make API call
tournamentJSON = urlopen("https://api.smash.gg/tournament/falcon-punch-fridays-46")

#tournamentJSON = urlopen(apiURL)

#TODO: Error check for when there is no set on stream currently

#Load json file into variable
tournamentData = json.load(tournamentJSON)

#Obtain tournament ID and name
tournamentID = tournamentData["entities"]["tournament"]["id"]
tournamentName = str(tournamentData["entities"]["tournament"]["name"])


#Construct URL of stream queue api call and open
streamURL = "https://api.smash.gg/station_queue/" + str(tournamentID)
streamJSON = urlopen(streamURL)

#For testing purposes, read local file for JSON
with open('FPF-Stream-Queue-Ex-poyovsrvr.json', 'r') as f:
	streamData = json.load(f)
f.close()

#Uncomment below for live stream again
#streamData = json.load(streamJSON) 

streamJSON.close()

#Extract data about players on stream

#Line below needs to be fixed
#tournamentRound = str(streamData["data"]["entities"]["sets"]["midRoundText"])
tournamentRound = "Fix later"

gamerTag1 = str(streamData["data"]["entities"]["player"][0]["gamerTag"])
twitter1 = str(streamData["data"]["entities"]["player"][0]["twitterHandle"])

gamerTag2 = str(streamData["data"]["entities"]["player"][1]["gamerTag"])
twitter2 = str(streamData["data"]["entities"]["player"][1]["twitterHandle"])

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


