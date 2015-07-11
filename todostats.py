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

statsfile = open(filename, 'r')
projects = defaultdict(int)
pattern = re.compile('@[a-zA-Z0-9]+')
start_date = re.compile('[0-9-]')

today = datetime.datetime.today()
last_monday = today - datetime.timedelta(days=-today.weekday(), weeks=1)
print "Tasks done between"
print last_monday.strftime("%Y-%m-%d")
print today.strftime("%Y-%m-%d")
print "\n"

for i in statsfile:
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

statsfile.close()
