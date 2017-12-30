from urllib.request import urlopen
import json

print("Code is running")

#Open URL to make API call
tournamentJSON = urlopen("https://api.smash.gg/tournament/falcon-punch-fridays-46")
#Load json file into variable
tournamentData = json.load(tournamentJSON)

#Obtain tournament ID
tournamentID = tournamentData["entities"]["tournament"]["id"]


#print(tournamentID) #Test successful, tournament ID is correct

#Construct URL of stream queue api call and open
streamURL = "https://api.smash.gg/station_queue/" + str(tournamentID)

#print(streamURL) #Test successful, url is correct

streamJSON = urlopen(streamURL)

streamData = json.load(streamJSON)

#Extract data about players on stream
gamerTag0 = str(streamData["data"]["entities"]["player"][0]["gamerTag"])
twitter0 = str(streamData["data"]["entities"]["player"][0]["twitterHandle"])

gamerTag1 = str(streamData["data"]["entities"]["player"][1]["gamerTag"])
twitter1 = str(streamData["data"]["entities"]["player"][1]["twitterHandle"])


print("Currently on stream: " + gamerTag0 + " (Twitter handle: " + twitter0 + ") vs. " + gamerTag1 + " (Twitter handle: " + twitter1 + ")")