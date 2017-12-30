from urllib.request import urlopen
import json

print("Code is running")

#Open URL to make API call
tournamentJSON = urlopen("https://api.smash.gg/tournament/falcon-punch-fridays-46")
#Load json file into variable
tournamentData = json.load(tournamentJSON)

#Obtain tournament ID and name
tournamentID = tournamentData["entities"]["tournament"]["id"]
tournamentName = str(tournamentData["entities"]["tournament"]["name"])


#Construct URL of stream queue api call and open
streamURL = "https://api.smash.gg/station_queue/" + str(tournamentID)


streamJSON = urlopen(streamURL)

streamData = json.load(streamJSON)

#Extract data about players on stream
tournamentStage = str(streamData["data"]["entities"]["sets"]["midRoundText"])

gamerTag0 = str(streamData["data"]["entities"]["player"][0]["gamerTag"])
twitter0 = str(streamData["data"]["entities"]["player"][0]["twitterHandle"])

gamerTag1 = str(streamData["data"]["entities"]["player"][1]["gamerTag"])
twitter1 = str(streamData["data"]["entities"]["player"][1]["twitterHandle"])


#print("Currently on stream: " + gamerTag0 + " (Twitter handle: " + twitter0 + ") vs. " + gamerTag1 + " (Twitter handle: " + twitter1 + ")")

#Print relevant information
print("Event name: " + tournamentName)
print("Stage of tournament on stream: " + tournamentStage)

print("Player 1 name: " + gamerTag0)
print("Player 1 twitter handle:  " + twitter0)

print("Player 2 name: " + gamerTag1)
print("Player 2 twitter handle:  " + twitter1)


