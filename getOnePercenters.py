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

def getPercenters(segmentID,startPercent,endPercent):
    numAthletes = getAthleteCount(segmentID)
    numPercenters = .01 * endPercent * numAthletes
    startInd = .01* startPercent *numAthletes

    leaders = []
    currPage = 0
    altFileName = segmentID+'.json'


    while len(leaders)+200 < numPercenters:
        currPage = currPage +1
        if os.path.isfile('leaderboard.json'):
            os.remove('leaderboard.json')
        if os.path.isfile(altFileName):
            os.remove(altFileName)
        a = set(os.listdir())
        url = 'http --download \"https://www.strava.com/api/v3/segments/'+str(segmentID)+'/leaderboard?page='+str(currPage)+'&per_page=200\" \"Authorization: Bearer 97d6ac23416cfc8444ca774e044f736415783efe\"'
        subprocess.run(url)
        b = set(os.listdir())
        newFileName = list(a.symmetric_difference(b))[0]
        print(newFileName)
        #if os.path.isfile(altFileName):
        with open(newFileName,encoding='utf8') as f:
            data = json.load(f)
        """
        elif os.path.isfile('leaderboard.json'):
            with open('leaderboard.json',encoding='utf8') as f:
                data = json.load(f)
        """
        leaders.extend(data['entries'])

    return(leaders[int(startInd):int(numPercenters)])
