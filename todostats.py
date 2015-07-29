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

def calculate_dates(start_date=None, end_date=None):
    if end_date:
        end_date = convert_to_time(end_date)
    else:
        end_date = datetime.datetime.today()
    if start_date:
        start_date = convert_to_time(start_date)
    else:
        start_date = end_date - datetime.timedelta(days=end_date.weekday())

    return start_date, end_date

if __name__ == '__main__':
    start_date, end_date = calculate_dates(args.sd, args.ed)
    valid_dates = get_valid_dates(start_date, end_date)
    found_projects = get_valid_projects(valid_dates, args.f)
    print "Tasks done between " + start_date.strftime("%Y-%m-%d") + " - " + end_date.strftime("%Y-%m-%d")
    completed_tasks = get_completed_tasks(found_projects)
    output_stats(completed_tasks)
