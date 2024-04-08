#!/usr/bin/env python3
import re
import sys
import os

"""
Create a file with hours worked. Separate the hours and the minutes by a colon.

 Example:
cat theo_cincotta_07042024
4:23
1:30
0:03

 Run:
python3 hours_calculator.py theo_cincotta_07042024
Hours: 5
Minutes: 56
Total minutes: 356
Total hours: 5.94

This will ceate a file called theo_cincotta_07042024.log
"""

file_name = sys.argv[1]
hours = open(file_name)

file_name_log = file_name + '.log'

count_hours = []
count_minutes = []

def count_hours_minutes(hours):
    for hour in hours:
        add_hours = re.split('[-:]', hour)[0]
        add_hours = int(add_hours)
        #print(add_hours)
        count_hours.append(add_hours)
        #print(count_hours)
    
        add_minutes = re.split('[-:]', hour)[1]
        add_minutes = int(add_minutes)
        #print(add_minutes)
        count_minutes.append(add_minutes)
        #print(count_minutes)

count_hours_minutes(hours)

# Count up the hours.
count_hours = sum(count_hours)

# Count up the minutes.
count_minutes = sum(count_minutes)

# Divide the hours by 60 minutes
hour_in_minutes = count_hours * 60

# add the hour minutes and the minutes togeather
total_minutes = hour_in_minutes + count_minutes

# total minutes divided by 60
total_hours = total_minutes / 60
total_hours = format(total_hours, ".2f")

print("Hours: " + str(count_hours))
print("Minutes: " + str(count_minutes))
print("Total minutes: " + str(total_minutes))
print("Total hours: " + str(total_hours))

# If file exists, delete it.
if os.path.isfile(file_name_log):
    os.remove(file_name_log)

with open(file_name_log, 'a') as f:
    print("Hours: " + str(count_hours), file=f)
    print("Minutes: " + str(count_minutes), file=f)
    print("Total minutes: " + str(total_minutes), file=f)
    print("Total hours: " + str(total_hours), file=f)
