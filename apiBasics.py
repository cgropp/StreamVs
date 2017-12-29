from urllib.request import urlopen
import json

print("Code is running")

#Open URL to make API call
tournamentJSON = urlopen('https://api.smash.gg/tournament/mega-smash-mondays-126')
#Load json file into variable
tournamentData = json.load(tournamentJSON)

#Obtain tournament ID
tournamentID = tournamentData["entities"]["tournament"]["id"]


print(tournamentID) #Test successful, tournament ID is correct

#Construct URL of stream queue api call and open
streamQueueURL = "https://api.smash.gg/station_queue/" + str(tournamentID)
print(streamQueueURL)
streamQueueJSON = urlopen(streamQueueURL)