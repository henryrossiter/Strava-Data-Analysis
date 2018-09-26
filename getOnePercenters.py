import subprocess
import json
import os
import pprint

def getAthleteCount(segmentID):
    fileName = str(segmentID)+'.json'
    if not os.path.isfile(fileName):
        url = 'http GET \"https://www.strava.com/api/v3/segments/'+str(segmentID) +'\" \"Authorization: Bearer 97d6ac23416cfc8444ca774e044f736415783efe\"'
        subprocess.run(url.replace("GET","--download"))

    with open(fileName) as f:
        data = json.load(f)
    return(data['athlete_count'])

def getPercenters(segmentID,percent):
    numAthletes = getAthleteCount(segmentID)
    numPercenters = .01 * percent * numAthletes

    leaders = []
    currPage = 0

    while len(leaders) < numPercenters:
        currPage = currPage +1
        if os.path.isfile('leaderboard.json'):
            os.remove('leaderboard.json')
        url = 'http --download \"https://www.strava.com/api/v3/segments/'+str(segmentID)+'/leaderboard?page='+str(currPage)+'&per_page=100\" \"Authorization: Bearer 97d6ac23416cfc8444ca774e044f736415783efe\"'
        subprocess.run(url)

        with open('leaderboard.json',encoding='utf8') as f:
            data = json.load(f)
        leaders.extend(data['entries'])

    return(leaders)
