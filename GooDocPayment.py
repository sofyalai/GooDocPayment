#!/usr/bin/python

import sys
import gspread
import datetime
import webbrowser

# Variables
total = len(sys.argv)

def remove_row ():
    answer = raw_input("Are you sure you want to remove the last row from the spreadsheet? (y/n) ")
    if answer == 'y':
        worksheet.resize(len(values_list) - 1)
    print "Removed last row from spreadsheet."
    
def open_in_web_browser ():
    controller = webbrowser.get('Firefox')
    controller.open('https://docs.google.com/spreadsheet/ccc?key=0Al7r6sbzIbfsdGhTcEJ1SEpkZnVMTTBJc0JVYlc5NVE#gid=0')
    print "Page opened in browser."

def program_exit ():
    print "Too few arguments, try again. Type 'help' to get help."
    sys.exit()
    
# Get command line arguments
def get_args (arg_list):
    
    if total > 1:
        arg = str(arg_list[1])  # convert to string
    else:
        program_exit()        

    if arg == "rm":
        remove_row()
    elif arg == "open":
        open_in_web_browser()
    elif (arg == "f") or (arg == "y"):
        name = arg
        if total > 2:
            value = str(arg_list[2])
            if total > 3:
                date = str(arg_list[3])
            else:
                localtime = datetime.datetime.now()
                date = "%d-%d-%d" % (localtime.year, localtime.month, localtime.day)
            update_Data(name, value, date)
        else:
            program_exit()

# update data main function
def update_Data (name, value, date):
    # assign col
    if name == 'f':
        col = 2
    elif name == 'y':
        col = 3

    # assign row
    row = len(values_list) + 1

    # insert 1 row
    worksheet.add_rows(1)
    # assign now_date

    # input date to cell
    worksheet.update_cell(row, 1, date)

    # input cash amount to cell
    worksheet.update_cell(row, col, str(value))
            
    # fetch the total value from worksheet
    # conver val to float number)
    val = worksheet.acell('D2').value

    if val > 0:
        print ("Ying-Chun owes :%s kr" % val)
    else:
        print ("Fredrik owes :%s kr" % val)

# User input
account_input = raw_input('your account: ')
password_input = raw_input('your password: ')
gc = gspread.login(account_input, password_input) 

# assign worksheet
sht1 = gc.open_by_key('0Al7r6sbzIbfsdGhTcEJ1SEpkZnVMTTBJc0JVYlc5NVE')
worksheet = sht1.sheet1

# fetch values of the 1st colum
values_list = worksheet.col_values(1)

get_args(sys.argv)
