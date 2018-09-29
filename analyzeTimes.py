from pandas import Series
import pandas as pd
from matplotlib import pyplot
import numpy

def getListOfStartHours(segmentID):
    import getOnePercenters
    record = getOnePercenters.getPercenters(segmentID,0,100)
    startHourList = []
    for guy in record:
        startHourList.append(int(guy['start_date_local'][11:13]))
    newFileName = segmentID+'.txt'
    numpy.savetxt(newFileName,startHourList)
    return(startHourList)

# takes an array of items to plot, each item in format: [{segment id},{end pct}]
def plotTime(records):

    startTimeList = []
    for segmentID in records:
        seekedFileName = str(segmentID[0])+'.txt'
        hourArr = numpy.loadtxt(seekedFileName)
        stopInd = int(len(hourArr)*segmentID[1]*.01)
        hourArr = hourArr[:stopInd]
        startTimeList.append(hourArr)
        print(hourArr)

    fig, ax = pyplot.subplots()
    maxStartTime = max([max(sublist) for sublist in startTimeList])
    minStartTime = min([min(sublist) for sublist in startTimeList])
    num_bins = int(maxStartTime-minStartTime)
    print(num_bins)
    n, bins, patches = pyplot.hist(startTimeList, num_bins, rwidth=.8, density=True, color=['#fc4c02','#000000','#555555'], alpha=0.8, edgecolor='#000000')


    ax.set_title('Three Sisters: New York, NY')
    ax.set_xlabel('Activity Start Hour')
    ax.set_ylabel('Fraction of Efforts')
    ax.set_xticks([5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])
    ax.set_yticks([.1,.2,.3,.4,.5,.6,.7], minor = False)
    ax.set_yticks([.02,.04,.06,.08,.12,.14,.16,.18,.22,.24,.26,.28,.32,.34,.36,.38,.42,.44,.46,.48,.52,.54,.56,.58,.62,.64], minor= True)
    ax.set_xlim(left = 4, right= 21)
    ax.set_ylim(bottom = 0, top = .64)
    ax.grid(True, which='major', alpha=.6, linestyle='-')
    ax.grid(True, which='minor', alpha=.2, linestyle='-')
    ax.legend(['Top 1% Efforts', 'Top 10% Efforts','Top 50% Efforts'])
    #ax.tick_params(labelcolor='r', labelsize='medium', width=3)

    pyplot.show()

plotTime([['648048',1],['648048',10],['648048',50]])
