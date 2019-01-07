#!/usr/bin/python

def main():

	counter = 0
	try:
		f=open('filename1.txt')
		x=1/0
	except FileNotFoundError as e:
		counter +=1
		print ('problem is ', e)
	except ZeroDivisionError as e:
		counter +=1
		# print ('A problem occured!', e)
		pass
	except:
		print ("unknown error")
	finally:
		print ('there were %d errors in the process' % counter)
		print ('ERRRRROOOORORORORO')

main()