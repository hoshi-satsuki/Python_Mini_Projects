# Lesson 3.2: Use Functions
# Mini-Project: Take a Break

# Write a program that prompts the user to take a break
# once every two hours, a maximum of three times.

# Use this space to describe your approach to the problem.
#
#
#
#

# Your code here.

import webbrowser
import time

number_breaks=3
interval_breaks=5


print "Program started on "+time.ctime()
break_count=0
while break_count<number_breaks:
    time.sleep(interval_breaks)
    webbrowser.open("https://www.youtube.com/watch?v=uMeR2W19wT0")
    break_count+=1
