import time
import LeetcodeAPI
import json
import os
import random
import pathlib

WIN_TITLE = "LeetApp"
WIN_WIDTH = 500
WIN_HEIGHT = 400
NUM_ALG_CHALLENGES = len(LeetcodeAPI.problems)
APP_NAME = "LeetCode Tracker"
SAVE_FILE_NAME = "leetconfig.json"
LANGUAGES = ["Java", "Python", "C++", "C"]

jsonData = {}

def configJsonFile(file):
    data = {}
    data["completed"] = {}
    data["numAlgorithms"] = NUM_ALG_CHALLENGES
    json.dump(data, file)
    
def parseSaveFile():
    global jsonData

    try:
        saves = open(SAVE_FILE_NAME,'r')
    except:
        saves = open(SAVE_FILE_NAME, 'w')
        configJsonFile(saves)
        saves.close()

    with open(SAVE_FILE_NAME, 'r') as saves:
        jsonData = json.load(saves)
        saves.close()

def makeDir(challengeNumber):
    pathlib.Path(os.path.join(os.getcwd(), "Solutions/" + str(challengeNumber))).mkdir(parents=True, exist_ok=True)

def getNextProblem():
    global jsonData

    nextChallenge = random.choice(list(LeetcodeAPI.problems.values()))
    while(nextChallenge.id in jsonData["completed"].keys() or not nextChallenge.free):
        nextChallenge = random.choice(list(LeetcodeAPI.problems.values()))

    return nextChallenge

#Leave it as a seperate function if for some reason I want to make it more complicated later.
def getRandomLanguage():
    return random.choice(LANGUAGES)