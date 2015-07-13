# todo.txt stats #

This is a simple script to show you some basic stats from your done.txt file.

## Installation ##

Get repo

    git clone https://github.com/dkns/todostats.git

## Usage ##

To get stats for all tasks done between various projects since last monday and today:

    python todostats.py -f ~/todo/done.txt

To print help run

    python todostats.py -h

## Neat ideas ##

Add it to cronjob and have it mail you summary every sunday at 23:59

## TODO ##

* Use argparse instead of argv
* Let user specify dates instead of always using first monday of week
* Output pretty graphs?
* More data:
* Tasks done in total
* Quarterly/yearly/monthly summary
* Longest open task
