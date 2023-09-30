# Alexander Hart 9/30/2023
# This program keeps track of your paycheck. 

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


clock_in = ''

clock_out = ''

lunch_break = ''

route_number = ''

truck_number = ''

