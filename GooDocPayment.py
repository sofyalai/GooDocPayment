#!/usr/bin/python

import sys
import gspread
import datetime
import webbrowser

total = len(sys.argv)

# User input
account_input = raw_input('your account: ')
password_input = raw_input('your password: ')
gc = gspread.login(account_input, password_input) 

# assign worksheet
sht1 = gc.open_by_key('0Al7r6sbzIbfsdGhTcEJ1SEpkZnVMTTBJc0JVYlc5NVE')
worksheet = sht1.sheet1

# fetch values of the 1st colum
values_list = worksheet.col_values(1)

# update data main function
def update_Data():
    # assign col
    if str(sys.argv[1])=='f':
        col=2
    elif str(sys.argv[1])=='y':
        col=3

    # assign row
    row = len(values_list)+1

    # insert 1 row
    worksheet.add_rows(1)
    # assign now_date
    if total == 4:
        now_date = str(sys.argv[3])
    else:
        localtime = datetime.datetime.now()
        now_date = "%d-%d-%d" % (localtime.year, localtime.month, localtime.day)
    # input date to cell
    worksheet.update_cell(row, 1, now_date)

    # input cash amount to cell
    worksheet.update_cell(row, col, str(sys.argv[2]))
            
    # fetch the total value from worksheet
    # conver val to float number)
    val = worksheet.acell('D2').value
    if val>0 :
        print ("Ying-Chun owes :%s kr" % val)
    else:
        print ("Fredrik owes :%s kr" % val)



if str(sys.argv[1]) == "rm" : #remove last row
    worksheet.resize(len(values_list)-1)
elif str(sys.argv[1]) == "open" : # open sheet in firefox
    controller = webbrowser.get('Firefox')
    controller.open('https://docs.google.com/spreadsheet/ccc?key=0Al7r6sbzIbfsdGhTcEJ1SEpkZnVMTTBJc0JVYlc5NVE#gid=0')
else: # update data
    update_Data();

