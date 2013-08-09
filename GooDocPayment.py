#!/usr/bin/python

import sys
import gspread
import datetime
import webbrowser

# User input
account_input = raw_input('your account: ')
password_input = raw_input('your password: ')

gc = gspread.login(account_input, password_input) 
sht1 = gc.open_by_key('0Al7r6sbzIbfsdGhTcEJ1SEpkZnVMTTBJc0JVYlc5NVE')

# assign worksheet
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
    if len(sys.argv) == 4:
        now_date = str(sys.argv[3])
    else:
        localtime = datetime.datetime.now()
        now_date = "%d-%d-%d" % (localtime.year, localtime.month, localtime.day)
    # input date to cell
    worksheet.update_cell(row, 1, now_date)

    # input cash amount to cell
    worksheet.update_cell(row, col, str(sys.argv[2]))

            
# fetch the total value from worksheet
def fetch_balance():
    val = worksheet.acell('D2').value
    val = val.replace(",",".")
    val = round(float(val),2)
    
    if val>0 :
        print ("Y owes :%f kr" % val)
    else:
        print ("F owes :%f kr" % abs(val))



if str(sys.argv[1]) == "rm" : #remove last row
    worksheet.resize(len(values_list)-1)
elif str(sys.argv[1]) == "open" : # open sheet in firefox
    controller = webbrowser.get('Firefox')
    controller.open('https://docs.google.com/spreadsheet/ccc?key=0Al7r6sbzIbfsdGhTcEJ1SEpkZnVMTTBJc0JVYlc5NVE#gid=0')
elif str(sys.argv[1])== "b":
    fetch_balance();
elif str(sys.argv[1])== "help":
    print "./GooDocPayment [option] [arg0], [arg1]"
    print "  [option]"
    print "    rm   : remove the last row"
    print "    open : open the spreadsheet in Firefox"
    print "    b    : print the balance in terminal"
    print "    y|f  : update payment to spreadsheet"
    print "      - arg 0 : input payment amount. It can be a number or a formula, ex 500, =600-3"
    print "      - arg 1 : input the date, ex 12/30. it assign to today if no input. (optional)"
else: # update data
    update_Data();
    fetch_balance();

