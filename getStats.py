import numpy

def getPercentStats(pct, segID):
    seekedFileName = str(segID)+'.txt'
    hourArr = numpy.loadtxt(seekedFileName)
    stopInd = int(len(hourArr)*pct*.01)
    hourArr = hourArr[:stopInd]
    print('mean: ')
    print(numpy.mean(hourArr))
    print('\nstd: ')
    print(numpy.std(hourArr))

getPercentStats(100, 648048)
