import numpy
from matplotlib import pyplot

def chunkIt(seq, num):
    return(numpy.array_split(seq,num))

def getDeciles(arr):
    retArr = []
    for chunk in chunkIt(arr,10):
        retArr.append(sum(chunk)/len(chunk))
    return(retArr)

def plotDeciles(deciles, labs):
    fig, ax = pyplot.subplots()
    colors = ['#fc4c02','#ff8451','#b5b5b5','606060','000000']
    if not len(labs) == len(deciles):
        print("array of deciles must be same as length of label array!!")
    for i in range(len(deciles)):
        pyplot.plot(deciles[i], label=labs[i], color = colors[i], linewidth = 2.5, marker=".")
    ax.set_xlabel('Leaderboard Decile')
    ax.set_ylabel('Average Start Time')
    ax.set_title('Attempt Start Time by Leaderboard Spot')
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
    segDecs.append(getDeciles(hourArr))


plotDeciles(segDecs,segNames)
#pyplot.show()
