from collections import defaultdict
from sys import argv
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

for i in statsfile:
    project_name = pattern.search(i)
    if project_name:
        projects[project_name.group(0)] += 1
    else:
        projects["general"] += 1

# print "Week {} {}"
for i, k in projects.items():
    print "Tasks done for project {} : {}".format(i, k)

print "Tasks done in total: {}".format(sum(projects.values()))
print "Good job!"

statsfile.close()
