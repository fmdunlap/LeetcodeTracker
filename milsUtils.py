import datetime

def getStopwatchString(millis):
    mils = millis % 1000
    secs = (millis / 1000) % 60
    mins = ((millis / 1000) / 60) % 60
    hours = ((millis / 1000) / 60) / 60

    return "%i:%02i:%02i.%03i" % (hours,mins,secs,mils)

def getDayString(millis):
    line = ""
    line += str(datetime.datetime.fromtimestamp(millis//1000.0))
    return line.split(' ')[0]