# Alexander Hart 9/30/2023
# This program keeps track of your paycheck. 
# https://github.com/alexanderhart76/USPSInformationTracker


# use functions when code is action focused 
# use classes when code is state focused


'''
Every day I want to:

Input the time that I clocked in
Input the length of my lunch break, if I took one
Input the route # for whatever route I delivered that day
Input the truck # that I took
Input whatever notes I had along that route, such as problematic addresses 

I want it to output:

Hours worked on a given day
Hours worked on a given week
Hours worked on a given month
Hours worked total

It should calculate my pay on a given day, week, month, while taking into account:

Overtime pay
Hazard pay
Taxes

'''


import tkinter as tk
import datetime

# variables

clock_in = ''

clock_out = ''

lunch_break = ''

route_number = ''

truck_number = ''


# Main window
main_window = tk.Tk()
main_window.title('USPS Tracker')
main_window.mainloop()

# Settings window 
settings_window = tk.Tk()
settings_window.title('Settings')


# Calculates paycheck
def calculate_paycheck():
    return

# Database

