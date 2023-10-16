import tkinter as tk
import Paycheck_Calculator as pc
import unittest

class TestPaycheckCalculator(unittest.TestCase):

    def test_valid_inputs(self): 
        root = tk.Tk()
        app = pc.Week_Window(root)  
        
        app.friday_clock_in.insert('1:00am')
        app.friday_clock_out.insert('6:00pm')

        app.saturday_clock_in.insert('2:00am')
        app.saturday_clock_out.insert('7:00pm')

        app.sunday_clock_in.insert('3:00am')
        app.sunday_clock_out.insert('8:00pm')

        app.monday_clock_in.insert('4:00am')
        app.monday_clock_out.insert('9:00pm')

        app.tuesday_clock_in.insert('5:00am')
        app.tuesday_clock_out.insert('10:00pm')

        app.wednesday_clock_in.insert('6:00am')
        app.wednesday_clock_out.insert('11:00pm')

        app.thursday_clock_in.insert('7:00am')
        app.thursday_clock_out.insert('11:30pm')

        app.calculate_paycheck()

        # Checks the total paycheck
        self.assertEqual(app.total_paycheck_label.cget('text'), '2797.36') 

        # Checks the total hours worked
        self.assertEqual(app.total_hours_worked_label.cget('text'), '118.00 hours') 

        # Checks the total tax paid
        self.assertEqual(app.total_taxes_paid_label.cget('text'), '$709.42') 



    def test_checkmarks(self):
        root = tk.Tk()
        app = pc.Week_Window(root)  
        
        app.friday_clock_in.insert('1:00am')
        app.friday_clock_out.insert('6:00pm')
        app.took_lunch_friday.set(True)

        app.saturday_clock_in.insert('2:00am')
        app.saturday_clock_out.insert('7:00pm')
        app.took_lunch_saturday.set(True)

        app.sunday_clock_in.insert('3:00am')
        app.sunday_clock_out.insert('8:00pm')
        app.took_lunch_sunday.set(True)

        app.monday_clock_in.insert('4:00am')
        app.monday_clock_out.insert('9:00pm')
        app.took_lunch_monday.set(True)

        app.tuesday_clock_in.insert('5:00am')
        app.tuesday_clock_out.insert('10:00pm')
        app.took_lunch_tuesday.set(True)

        app.wednesday_clock_in.insert('6:00am')
        app.wednesday_clock_out.insert('11:00pm')
        app.took_lunch_wednesday.set(True)

        app.thursday_clock_in.insert('7:00am')
        app.thursday_clock_out.insert('11:30pm')
        app.took_lunch_thursday.set(True)

        app.calculate_paycheck()

        # Checks the total paycheck
        self.assertEqual(app.total_paycheck_label.cget('text'), '2704.26') 

        # Checks the total hours worked
        self.assertEqual(app.total_hours_worked_label.cget('text'), '115.00 hours') 

        # Checks the total tax paid
        self.assertEqual(app.total_taxes_paid_label.cget('text'), '$685.81') 


unittest.main()