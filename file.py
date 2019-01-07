#!/usr/bin/python

import os
import sys

print (sys.platform)
print (os.name)

print list("elo")

def functionName(level):
   	if level == 13:
		raise "Invalid level!", level

for i in range(10,15):
	functionName(i)
	try:
   		print i
	except "Invalid level!":
   		print "nieszczesliwa \n"
	else:
   		print " dobrze \n"
	

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# del dict['Name']; # remove entry with key 'Name'
print dict.get('Name')
dict.clear();     # remove all entries in dict

print dict

Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   global Money
   Money = Money + 1

print Money
AddMoney()
print Money

try:
   fh = open("testfile", "w")
   try:
      fh.write("This is my test file for exception handling!!\n")
   finally:
      print "Going to close the file"
      fh.close()
except IOError:
   print "Error: can\'t find file or read data"

a = ['hi', 'there', 'ok']
result = ''
for i in range(len(a)):
    # i will be 0, 1, 2 ... use a[i] to look at each element.
    # Here we just accumulate the a[i] strings
    result = result + a[i] + " "
print result