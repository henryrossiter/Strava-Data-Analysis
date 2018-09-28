from analyzeTimes import getListOfStartHours


with open('segments.txt') as f:
    content = f.readlines()
for x in content:
    getListOfStartHours(x.strip())
