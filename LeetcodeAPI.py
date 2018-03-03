from lxml import html
import requests
import json
import pprint as pp
import milsUtils

#Color boxes for Difficulty

difficultySquare = ["N/A", "![#07c117](https://placehold.it/15/07c117/000000?text=+)", "![#e5de19](https://placehold.it/15/e5de19/000000?text=+)", "![#ad1414](https://placehold.it/15/ad1414/000000?text=+)"]

#Load in JSON data from Leetcode
api_qs = requests.get('https://leetcode.com/api/problems/all/')
problem_json = json.loads(api_qs.text)

intro = """# LeetApp - An Automatic Status Journal of your Practice Progress
Thanks for checking out LeetApp - right now I'm mostly just using it myself for practice, but I'm constantly adding features. Feel free to help out, or use it as you wish!

Usage
======
To use, download the repo and unzip. Then run the following in a terminal in that directory.

`python3 ./LeetApp.py`

My Progress
======
"""

class problem:
    def __init__(self, problem_info):
        self.frontend_id = problem_info['stat']['frontend_question_id']
        self.id = problem_info['stat']['question_id']
        self.slug = problem_info['stat']['question__title_slug']
        self.name = problem_info['stat']['question__title']
        self.difficulty = problem_info['difficulty']['level']
        self.free = not problem_info['paid_only']
        self.pass_rate = problem_info['stat']['total_acs']/problem_info['stat']['total_submitted']

def getMDLine(app_json, p):
    line = ""
    # Ah yes. Type safety.
    idStr = str(p.id)

    line += "Problem %i: %s   %s\n" %(p.frontend_id, p.name, difficultySquare[p.difficulty])
    line += "------\n"
    if(idStr in app_json['completed'].keys()):
        line += "* **Status:** COMPLETE!\n"
        line += "* **Time Taken:** %s\n" % milsUtils.getStopwatchString(app_json['completed'][idStr]['elapsed'])
        line += "* **Completed On:** %s\n" % milsUtils.getDayString(app_json['completed'][idStr]['start'])
    else:
        line += "* **Status:** INCOMPLETE\n* **Time Taken:** N/A \n* **Completed On:** N/A\n"

    line +='\n'
        
    return line

def getProblemURL(p):
    return "https://leetcode.com/problems/" + p.slug

def writeReadme(app_json):
    with open("README.md", "w") as f:
        f.write(intro)
        for problem in problems.values():
            f.write(getMDLine(app_json, problem))

        f.close()

def debugPrintLeetAPIJSON():
    pp.pprint(problem_json)

#Initialization code
problems = {}
for p in problem_json['stat_status_pairs']:
    newProblem = problem(p)
    problems[newProblem.id] = newProblem