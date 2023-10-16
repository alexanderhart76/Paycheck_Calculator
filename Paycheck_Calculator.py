#Alexander Hart 10/15/2023

''' This is a Paycheck calculator that takes in clock-ins and clock-outs for a work week and outputs the amount of hours worked, your paycheck after taxes
and how much in tax you paid. '''
import os
import tkinter as tk
from datetime import datetime
import json
from PIL import Image, ImageTk

# Variables
hourly_wage = 22.23 # Represents how much you get paid per hour in dollars and cents.
income_tax = 12.58 # Represents how much income tax you pay. 12.58% is 12.58.
fica_tax = 7.65 # Represents how much in social security + medicare tax you pay. 7.65% is 7.65.
overtime_pay = 1.5 # This number is multiplied by your hourly_wage to represent your overtime wage for hours worked after 40 hours.  

settings_file = "variables.json" # When you change the variables in the settings window it is saved in this file


''' This is the settings window where users can change the variables hourly_wage, income_tax, fica_tax and overtime_pay from the gui  '''

# Settings window that lets you change the variables from the gui
class Settings_Window(tk.Toplevel):
        def __init__(self, master = None):
            super().__init__(master = master)
            self.title("Settings")
            self.iconbitmap("dollar.ico")

# Current Settings Labels
            tk.Label(self, text="Current settings").grid(row= 0, column=0, columnspan = 2, padx=0, pady=0)
            
            # Hourly Wage 
            tk.Label(self, text="Hourly wage:").grid(row=1 , column=0, padx=0, pady=0)
            self.hourly_wage_label = tk.Label(self, text=str(hourly_wage))
            self.hourly_wage_label.grid(row= 1, column=1)

            # Income Tax 
            tk.Label(self, text="Income tax:").grid(row= 2, column=0, padx=0, pady=0)
            self.income_tax_label = tk.Label(self, text=str(income_tax))
            self.income_tax_label.grid(row= 2, column=1)

            # FICA Tax 
            tk.Label(self, text="FICA tax:").grid(row= 3, column=0, padx=0, pady=0)
            self.fica_tax_label = tk.Label(self, text=str(fica_tax))
            self.fica_tax_label.grid(row= 3, column=1)

            #Overtime 
            tk.Label(self, text="Overtime:").grid(row= 4, column=0, padx=0, pady=0)
            self.overtime_pay_label = tk.Label(self, text=str(overtime_pay))
            self.overtime_pay_label.grid(row= 4, column=1)


# Change Settings Labels
            tk.Label(self, text="Change settings:").grid(row= 5, column=0, columnspan = 2, padx=0, pady=0)

            # Hourly Wage
            tk.Label(self, text ="Hourly wage:").grid(row=6,column=0)
            self.hourly_wage = tk.Entry(self)
            self.hourly_wage.grid(row=6, column=1)

            # Income Tax
            tk.Label(self, text ="Income tax:").grid(row=7,column=0)
            self.income_tax = tk.Entry(self)
            self.income_tax.grid(row=7, column=1)

            # FICA Tax
            tk.Label(self, text ="FICA tax:").grid(row=8,column=0)
            self.fica_tax = tk.Entry(self)
            self.fica_tax.grid(row=8, column=1)

            # Overtime Pay
            tk.Label(self, text ="Overtime pay:").grid(row=9,column=0)
            self.overtime_pay = tk.Entry(self)
            self.overtime_pay.grid(row=9, column=1)
            
# Buttons
            # Apply Settings Button
            self.apply_settings_button = tk.Button(self, text='Apply Settings', command=self.apply_settings)
            self.apply_settings_button.grid(row=10, column=0, padx=10, pady=10)

            # Help Button
            self.back_button = tk.Button(self, text='Help', command=self.open_readme)
            self.back_button.grid(row=10, column=1, padx=10, pady=10)

        # Applys new settings, is run after the "Apply Settings" button is clicked
        def apply_settings(self):
            global hourly_wage, income_tax, fica_tax, overtime_pay

             # Checks if the input fields are empty and set the values to 0 if they are. Also sets setting to 0 if entry field throw ValueError. 
            try:
                hourly_wage = float(self.hourly_wage.get())
                if hourly_wage < 0:
                    hourly_wage = 0
            except ValueError:
                hourly_wage = 0
            self.hourly_wage_label.config(text=str(hourly_wage))

            try:
                income_tax = float(self.income_tax.get())
                if income_tax < 0:
                    income_tax = 0
            except ValueError:
                income_tax = 0
            self.income_tax_label.config(text=str(income_tax))

            try:
                fica_tax = float(self.fica_tax.get())
                if fica_tax < 0:
                    fica_tax = 0
            except ValueError:
                fica_tax = 0
            self.fica_tax_label.config(text=str(fica_tax))

            try:
                overtime_pay = float(self.overtime_pay.get())
                if overtime_pay < 0:
                    overtime_pay = 0
            except ValueError:
                overtime_pay = 0
            self.overtime_pay_label.config(text=str(overtime_pay))

            # Updates current settings labels with the new values
            self.hourly_wage_label.config(text=str(hourly_wage))
            self.income_tax_label.config(text=str(income_tax))
            self.fica_tax_label.config(text=str(fica_tax))
            self.overtime_pay_label.config(text=str(overtime_pay))
            
            # Updates global variables
            hourly_wage = hourly_wage
            income_tax = income_tax
            fica_tax = fica_tax
            overtime_pay = overtime_pay

            save_settings()

        def open_readme(self):
            readme_file = os.path.join(os.path.dirname(__file__), 'README.txt')
            if os.path.exists(readme_file):
                os.startfile(readme_file)
            else:
                print("README.txt file not found.")

            



''' This is the main window where users can input their clock-ins and clock-outs, and see the output.'''
    
# Main Window
class Week_Window:
    def __init__(self, master):
        self.master = master 
        load_settings() # loads settings from json
        master.title('Paycheck Calculator') # window title
        master.iconbitmap("dollar.ico") # window icon

        # Contains the title image "Paycheck Calculator"
        title_image = Image.open("title_image.png")
        logo = ImageTk.PhotoImage(title_image)
        image_label = tk.Label(root, image=logo)
        image_label.image = logo
        image_label.grid(row = 0, columnspan = 4)        

        # Clock-In Label
        tk.Label(master, text='Clock-In Time', font=('Helvetica', 10)).grid(row=1, column=1, sticky='n')

        # Clock-Out Label
        tk.Label(master, text='Clock-Out Time', font=('Helvetica', 10)).grid(row=1, column=2, sticky='n')

        # Took Lunch? Label
        tk.Label(master, text='Lunch?', font=('Helvetica', 10)).grid(row=1, column=3, sticky='n')

# Friday
        tk.Label(master, text='Friday').grid(row=2, column=0, sticky='w')
        self.friday_clock_in = tk.Entry(master)
        self.friday_clock_in.grid(row=2, column=1)

        self.friday_clock_out = tk.Entry(master)
        self.friday_clock_out.grid(row=2, column=2)

        self.took_lunch_friday= tk.BooleanVar()
        self.took_lunch= tk.Checkbutton(master, variable = self.took_lunch_friday)
        self.took_lunch.grid(row=2, column=3)

# Saturday
        tk.Label(master, text='Saturday').grid(row=3, column=0, sticky='w')
        self.saturday_clock_in = tk.Entry(master)
        self.saturday_clock_in.grid(row=3, column=1)

        self.saturday_clock_out = tk.Entry(master)
        self.saturday_clock_out.grid(row=3, column=2)

        self.took_lunch_saturday= tk.BooleanVar()
        self.took_lunch = tk.Checkbutton(master, variable = self.took_lunch_saturday)
        self.took_lunch.grid(row=3, column=3)

# Sunday
        tk.Label(master, text='Sunday').grid(row=4, column=0, sticky='w')
        self.sunday_clock_in = tk.Entry(master)
        self.sunday_clock_in.grid(row=4, column=1)
        
        self.sunday_clock_out = tk.Entry(master)
        self.sunday_clock_out.grid(row=4, column=2)

        self.took_lunch_sunday= tk.BooleanVar()
        self.took_lunch = tk.Checkbutton(master, variable = self.took_lunch_sunday)
        self.took_lunch.grid(row=4, column=3)

# Monday
        tk.Label(master, text='Monday').grid(row=5, column=0, sticky='w')
        self.monday_clock_in = tk.Entry(master)
        self.monday_clock_in.grid(row=5, column=1)

        self.monday_clock_out = tk.Entry(master)
        self.monday_clock_out.grid(row=5, column=2)

        self.took_lunch_monday= tk.BooleanVar()
        self.took_lunch = tk.Checkbutton(master, variable = self.took_lunch_monday)
        self.took_lunch.grid(row=5, column=3)

# Tuesday
        tk.Label(master, text='Tuesday').grid(row=6, column=0, sticky='w')
        self.tuesday_clock_in = tk.Entry(master)
        self.tuesday_clock_in.grid(row=6, column=1)

        self.tuesday_clock_out = tk.Entry(master)
        self.tuesday_clock_out.grid(row=6, column=2)

        self.took_lunch_tuesday= tk.BooleanVar()
        self.took_lunch = tk.Checkbutton(master, variable = self.took_lunch_tuesday)
        self.took_lunch.grid(row=6, column=3)

# Wednesday
        tk.Label(master, text='Wednesday').grid(row=7, column=0, sticky='w')
        self.wednesday_clock_in = tk.Entry(master)
        self.wednesday_clock_in.grid(row=7, column=1)
        
        self.wednesday_clock_out = tk.Entry(master)
        self.wednesday_clock_out.grid(row=7, column=2)

        self.took_lunch_wednesday= tk.BooleanVar()
        self.took_lunch = tk.Checkbutton(master, variable = self.took_lunch_wednesday)
        self.took_lunch.grid(row=7, column=3)

# Thursday
        tk.Label(master, text='Thursday').grid(row=8, column=0, sticky='w')
        self.thursday_clock_in = tk.Entry(master)
        self.thursday_clock_in.grid(row=8, column=1)

        self.thursday_clock_out = tk.Entry(master)
        self.thursday_clock_out.grid(row=8, column=2)

        self.took_lunch_thursday= tk.BooleanVar()
        self.took_lunch = tk.Checkbutton(master, variable = self.took_lunch_thursday)
        self.took_lunch.grid(row=8, column=3)

# Buttons

        #Calculate Paycheck Button
        self.clock_in_button = tk.Button(master, text='Calculate', command=self.calculate_paycheck)
        self.clock_in_button.grid(row=12, column=1, padx=0, pady=10)

        # Open Settings Button
        self.settings_button = tk.Button(master, text="Settings", command=self.open_settings_window)
        self.settings_button.grid(row=12, column=2, padx=0, pady=10)

# Total Paycheck, Tax Paid, Hours Worked Label, and Error Label
       
        tk.Label(master, text='Paycheck:').grid(row=9, column=1, sticky='w', padx=0, pady=0)
        self.total_paycheck_label = tk.Label(master, text='')
        self.total_paycheck_label.grid(row=9, column=2)

        tk.Label(master, text='Hours Worked:').grid(row=10, column=1, sticky='w', padx=0, pady=0)
        self.total_hours_worked_label = tk.Label(master, text='')
        self.total_hours_worked_label.grid(row= 10, column=2)

        tk.Label(master, text='Tax paid:').grid(row=11, column=1, sticky='w', padx=0, pady=0)
        self.total_taxes_paid_label = tk.Label(master, text='')
        self.total_taxes_paid_label.grid(row= 11, column=2)




    # Opens the setting window   
    def open_settings_window(self):
            self.open_settings_window = Settings_Window(master=self.master)

    # Calculates the amount of hours worked in a given shift
    def calculate_hours(self):

        # Here is where input strings representing the beginning and end of a shift are turned into digits using the datetime module
        def get_hours_from_strings(clock_in, clock_out):
            
            # Assigns 0 hours for a day if a user doesn't input AM or PM
            if ('am' not in clock_in and 'pm' not in clock_in) or ('am' not in clock_out and 'pm' not in clock_out):
                self.print_error()
            
            # Assigns 0 hours for a day if nothing is inputted
            if not clock_in or not clock_out:
                return 0
                    
            # Parses the clock in and clock out strings to a datetime objct
            try:
                clock_in_time = datetime.strptime(clock_in, "%I:%M%p")
                clock_out_time = datetime.strptime(clock_out, "%I:%M%p")
            except ValueError:
                self.print_error()
                
            # Ensures that clock_out_time is after clock_in_time
            if clock_out_time <= clock_in_time:
                self.print_error()
                raise ValueError("Clock out time cannot be before or equal to the clock in time.")
                

            # Gets digit reprsenting hours worked. There are 3600 seconds in an hour.
            total_hours_worked = (clock_out_time - clock_in_time).total_seconds() / 3600
            return total_hours_worked


       # Variables containing inputs we get from clock-in/ clock-out entrys
        friday_clock_in=self.friday_clock_in.get()
        saturday_clock_in=self.saturday_clock_in.get()
        sunday_clock_in=self.sunday_clock_in.get()
        monday_clock_in=self.monday_clock_in.get()
        tuesday_clock_in=self.tuesday_clock_in.get()
        wednesday_clock_in=self.wednesday_clock_in.get()
        thursday_clock_in=self.thursday_clock_in.get()
        

        friday_clock_out=self.friday_clock_out.get()
        saturday_clock_out=self.saturday_clock_out.get()
        sunday_clock_out=self.sunday_clock_out.get()
        monday_clock_out=self.monday_clock_out.get()
        tuesday_clock_out=self.tuesday_clock_out.get()
        wednesday_clock_out=self.wednesday_clock_out.get()
        thursday_clock_out=self.thursday_clock_out.get()

        # Sends those inputs to get_hours_from_strings for processing
        hours_worked_friday = get_hours_from_strings(friday_clock_in, friday_clock_out)
        hours_worked_saturday = get_hours_from_strings(saturday_clock_in, saturday_clock_out)
        hours_worked_sunday = get_hours_from_strings(sunday_clock_in, sunday_clock_out)
        hours_worked_monday = get_hours_from_strings(monday_clock_in, monday_clock_out)
        hours_worked_tuesday = get_hours_from_strings(tuesday_clock_in, tuesday_clock_out)
        hours_worked_wednesday = get_hours_from_strings(wednesday_clock_in, wednesday_clock_out)
        hours_worked_thursday = get_hours_from_strings(thursday_clock_in, thursday_clock_out)

        # Checks to see if took lunch, subtracts 30 minutes from total_hours_worked. Gets input from the checkmarks.
        if self.took_lunch_friday.get():
           hours_worked_friday -= 0.5
        
        if self.took_lunch_saturday.get():
           hours_worked_saturday -= 0.5

        if self.took_lunch_sunday.get():
           hours_worked_sunday -= 0.5
        
        if self.took_lunch_monday.get():
           hours_worked_monday -= 0.5
        
        if self.took_lunch_tuesday.get():
           hours_worked_tuesday -= 0.5

        if self.took_lunch_wednesday.get():
           hours_worked_wednesday -= 0.5

        if self.took_lunch_thursday.get():
           hours_worked_thursday -= 0.5

        # Adds up hours for all days
        total_hours_worked = hours_worked_friday + hours_worked_saturday + hours_worked_sunday + hours_worked_monday + hours_worked_tuesday + hours_worked_wednesday + hours_worked_thursday  # Add up hours for all days
        
        return total_hours_worked
    
# Calculates the paycheck
    def calculate_paycheck(self):
        total_hours_worked = self.calculate_hours()
        
        if total_hours_worked <= 40:
            # No overtime, regular pay
            paycheck_before_taxes = total_hours_worked * hourly_wage
        else:
            # Calculates regular pay (first 40 hours)
            regular_pay = 40 * hourly_wage
            # Calculates overtime pay (hours beyond 40, at 1.5 times the hourly wage)
            overtime_hours = total_hours_worked - 40
            overtime_pay = overtime_hours * (1.5 * hourly_wage)
            # Calculates total paycheck with regular and overtime pay
            paycheck_before_taxes = regular_pay + overtime_pay

        total_tax_paid = self.calculate_taxes(paycheck_before_taxes)
        paycheck_after_taxes = paycheck_before_taxes - total_tax_paid

        self.print_output(total_tax_paid, total_hours_worked, paycheck_after_taxes)


    # Calculates taxes
    def calculate_taxes(self, paycheck):
            income_tax_paid = (income_tax / 100) * paycheck
            fica_tax_paid = (fica_tax / 100) * paycheck
            total_tax_paid = income_tax_paid + fica_tax_paid
            return total_tax_paid
    
    # Prints output to the GUI labels 
    def print_output(self, total_tax_paid, total_hours_worked, paycheck_after_taxes):
        self.total_paycheck_label.config(text=f'${paycheck_after_taxes:.2f}')
        self.total_hours_worked_label.config(text=f'{total_hours_worked:.2f} hours')
        self.total_taxes_paid_label.config(text=f'${total_tax_paid:.2f}')

    # Prints error message
    def print_error(self):
        self.total_paycheck_label.config(text='Incorrect format')


''' Everything below is outside the class'''


# Function to save settings to json file
def save_settings():
    settings = {
        "hourly_wage": hourly_wage,
        "income_tax": income_tax,
        "fica_tax": fica_tax,
        "overtime_pay": overtime_pay
    }
    with open(settings_file, "w") as file:
        json.dump(settings, file)

# Function to load the settings from json fole
def load_settings():
    try:
        with open(settings_file, "r") as file:
            settings = json.load(file)
            global hourly_wage, income_tax, fica_tax, overtime_pay
            hourly_wage = settings["hourly_wage"]
            income_tax = settings["income_tax"]
            fica_tax = settings["fica_tax"]
            overtime_pay = settings["overtime_pay"]
    except (json.JSONDecodeError, FileNotFoundError):
        pass

# Executes the program
if __name__ == '__main__':
    load_settings() # loads settings from json
    root = tk.Tk()
    app = Week_Window(root)
    root.mainloop()