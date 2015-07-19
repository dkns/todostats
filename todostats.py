from collections import defaultdict
from time import mktime
import argparse
import datetime
import re
import sys
import time

parser = argparse.ArgumentParser(description="Print stats for todo.txt")
parser.add_argument('-f', '-filename', help='Location of done.txt file', type=file, required=True)
parser.add_argument('-sd', '-start-date', help="Start date for counting projects")
parser.add_argument('-ed', '-end-date', help="End date for counting projects")
args = parser.parse_args()

def convert_to_time(input_date):
    converted_date = time.strptime(input_date, "%Y-%m-%d")
    converted_date = datetime.datetime.fromtimestamp(mktime(converted_date))
    return converted_date

if args.ed:
    end_date = convert_to_time(args.ed)
else:
    end_date = datetime.datetime.today()

if args.sd:
    start_date = convert_to_time(args.sd)
else:
    start_date = end_date - datetime.timedelta(days=end_date.weekday())

def get_valid_dates(start_date, end_date):
    valid_dates = []
    delta = end_date - start_date
    for i in range(delta.days + 1):
        date = start_date + datetime.timedelta(days=i)
        valid_dates.append(date.strftime("%Y-%m-%d"))

    return valid_dates

def get_valid_projects(list_of_days, filename):
    found_projects = []
    for i in filename:
        for j in list_of_days:
            pattern = re.compile(j)
            found_project = pattern.search(i)
            if found_project:
                found_projects.append(i)

    return found_projects

valid_dates = get_valid_dates(start_date, end_date)
found_projects = get_valid_projects(valid_dates, args.f)

start_date = start_date.strftime("%Y-%m-%d")
today = end_date.strftime("%Y-%m-%d")
print "Tasks done between " + start_date + " - " + today

def get_completed_tasks(projects_list):
    projects = defaultdict(int)
    pattern = re.compile('@[a-zA-Z0-9]+')
    for i in projects_list:
        project_name = pattern.search(i)
        if project_name:
            projects[project_name.group(0)] += 1
        else:
            projects["general"] += 1

    return projects

def output_stats(tasks_done):
    for i, k in tasks_done.items():
        print "{} : {}".format(i, k)
    print "\n"
    print "Tasks done in total: {}".format(sum(tasks_done.values()))
    print "Good job!"

completed_tasks = get_completed_tasks(found_projects)
output_stats(completed_tasks)
