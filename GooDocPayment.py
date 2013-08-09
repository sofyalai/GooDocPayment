#!/usr/bin/python

import sys
import gspread

total = len(sys.argv)

cmdargs = str(sys.argv)

# print ("The total number of args pass:%d" % total)
# print ("Args list:%s" % cmdargs)

# print ("script name : %s" % str(sys.argv[0]))
# for i in xrange(total):
#     print ("arg # %d: %s" % (i,str(sys.argv[i])))

# User input
account_input = raw_input('your account: ')
input = raw_input('your password: ')

gc = gspread.login(account_input, input)

sht1 = gc.open_by_key('0Al7r6sbzIbfsdGhTcEJ1SEpkZnVMTTBJc0JVYlc5NVE')

# Select worksheet by index. Worksheet indexes start from zero
worksheet = sht1.get_worksheet(0)

# Most common case: Sheet1
worksheet = sht1.sheet1

val = worksheet.acell('D2').value

print val




