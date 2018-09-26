from pandas import Series
import pandas as pd
from matplotlib import pyplot

import getOnePercenters

def plotTime(records):
    startTimeList = []
    for guy in records:
        startTimeList.append(int(guy['start_date_local'][11:13]))

    num_bins = max(startTimeList)-min(startTimeList)
    n, bins, patches = pyplot.hist(startTimeList, num_bins, facecolor='blue', alpha=0.5)

    pyplot.show()

segmentID = '4653381'
onePercenters = getOnePercenters.getPercenters(segmentID,1)
fivePercenters = getOnePercenters.getPercenters(segmentID,5)
thirtyPercenters = getOnePercenters.getPercenters(segmentID,10)

plotTime(onePercenters)
plotTime(fivePercenters)
plotTime(thirtyPercenters)
