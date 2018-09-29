import numpy
from matplotlib import pyplot

def chunkIt(seq, num):
    return()

def getDecileMeans(arr):
    return([sum(chunk)/len(chunk) for chunk in numpy.array_split(arr,10)])

def getDecileMedians(arr):
    return([numpy.median(chunk) for chunk in numpy.array_split(arr,10)])

def plotDeciles(deciles, labs):
    fig, ax = pyplot.subplots()
    colors = ['#fc4c02','#ff8451','#b5b5b5','606060','000000']
    if not len(labs) == len(deciles):
        print("array of deciles must be same as length of label array!!")
    for i in range(len(deciles)):
        pyplot.plot(deciles[i], label=labs[i], color = colors[i], linewidth = 2.5, alpha=.9, marker=".")
    ax.set_xlabel('Leaderboard Decile')
    ax.set_ylabel('Average Start Time')
    ax.set_title('Attempt Start Time by Leaderboard Spot')
    ax.set_yticks([8,9,10,11,12,13,14])
    ax.set_yticklabels(['8 a.m.','9 a.m.','10 a.m.','11 a.m.','12 p.m.','1 p.m.','2 p.m.',])
    ax.set_xticks([0,1,2,3,4,5,6,7,8,9])
    ax.set_xticklabels(['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'])
    pyplot.legend(labs)
    pyplot.show()


with open('segments.txt') as f:
    segNums = f.readlines()
with open('segmentNames.txt') as n:
    segNames = n.readlines()
    segNames = [nam.strip() for nam in segNames]
segDecs = []
labs = []
for num in segNums:
    seekedFileName = num.strip()+'.txt'
    hourArr = numpy.loadtxt(seekedFileName)
    segDecs.append(getDecileMedians(hourArr))


plotDeciles(segDecs,segNames)
#pyplot.show()
