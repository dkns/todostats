from collections import defaultdict
from sys import argv # TODO use argparse
import datetime
import re
import sys

# TODO: decide whether to show all stats in total
# or just for this week
script, filename = argv

if not filename.endswith('.txt'):
    print "Please provide valid .txt file\n"
    print "Exiting"
    sys.exit(0)

today = datetime.datetime.today()
# last_monday = today - datetime.timedelta(days=today.weekday()) + datetime.timedelta(weeks=1)
last_monday = today - datetime.timedelta(days=today.weekday())
# last_monday = today + datetime.timedelta(days=(today.weekday() - 7) % 7, weeks=-1)
delta = today - last_monday
valid_dates = []

for i in range(delta.days + 1):
    date = last_monday + datetime.timedelta(days=i)
    valid_dates.append(date.strftime("%Y-%m-%d"))

found_projects = []
with open(filename) as f:
    lines = f.readlines()
    for i in lines:
        for j in valid_dates:
            pattern = re.compile(j)
            valid_project = pattern.search(i)
            if valid_project:
                found_projects.append(i)

last_monday = last_monday.strftime("%Y-%m-%d")
today = today.strftime("%Y-%m-%d")
print "Tasks done between " + last_monday + " - " + today

projects = defaultdict(int)
pattern = re.compile('@[a-zA-Z0-9]+')
for i in found_projects:
    project_name = pattern.search(i)
    if project_name:
        projects[project_name.group(0)] += 1
    else:
        projects["general"] += 1

for i, k in projects.items():
    print "{} : {}".format(i, k)

print "\n"
print "Tasks done in total: {}".format(sum(projects.values()))
print "Good job!"
