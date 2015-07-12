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
last_sunday = today - datetime.timedelta(days=7)
last_sunday = last_sunday.strftime("%Y-%m-%d")
today = today.strftime("%Y-%m-%d")

projects = defaultdict(int)
start_date = re.compile(last_sunday)
pattern = re.compile('@[a-zA-Z0-9]+')

found_projects = []

with open(filename) as f:
    lines = f.readlines()
    for i in lines:
        find_start = start_date.search(i)
        if find_start:
            # found_projects.append(i)
            print(find_start.group())
            break

print found_projects

print "Tasks done between " + last_sunday + " - " + today

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
