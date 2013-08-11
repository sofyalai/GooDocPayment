#!/usr/bin/python

import sys
import gspread
import datetime
import webbrowser

# Variables
var_list = dict(name=None, value=None, open_web=False, remove=False, date=None)
total = len(sys.argv)

# Get command line arguments
def get_args (arg_list, dict_list):
    arg = str(arg_list[1])  # convert to string
    if arg == "rm":
        dict_list['remove'] = True
    if arg == "open":
        print open
        dict_list['open_web'] = True
    if arg == "f":
        dict_list['name'] = arg
    if arg == "y":
        dict_list['name'] = arg
    # TODO: else here with exit program
            
    if dict_list['name'] != None:
        dict_list['value'] = str(arg_list[2])
    if total > 3:
        dict_list['date'] = str(arg_list[3])
    else:
        localtime = datetime.datetime.now()
        dict_list['date'] = "%d-%d-%d" % (localtime.year, localtime.month, localtime.day)
         

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

    # if total == 4:
    #     now_date = str(date)
    # else:    
    #     now_date = "%d-%d-%d" % (localtime.year, localtime.month, localtime.day)

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

get_args(sys.argv, var_list)

print var_list['name']

if var_list['remove'] == True: #remove last row
    answer = raw_input("Are you sure you want to remove the last row from the spreadsheet? (y/n) ")
    if answer == 'y':
        worksheet.resize(len(values_list) - 1)

elif var_list['open_web'] == True: # open sheet in firefox
    controller = webbrowser.get('Firefox')
    controller.open('https://docs.google.com/spreadsheet/ccc?key=0Al7r6sbzIbfsdGhTcEJ1SEpkZnVMTTBJc0JVYlc5NVE#gid=0')
    print "Page opened in browser"

elif var_list['name'] != None: # update data
    if var_list['value'] != 0:
        update_Data(var_list['name'], var_list['value'], var_list['date'])
        print "Name"
