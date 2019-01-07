#!/usr/bin/python

def main():
	try:
		# fh=open('filename1.txt')
		for line in readfile('filename1.txt'): print (line.strip())
	except IOError as e:
		print 'Could not open this file: ', e
	except ValueError as e:
		print 'Wrong file extension ', e
		

def readfile(filename):
	if filename.endswith(".txt"):
		fh = open(filename)
		return fh.readlines()
	else: 
		raise ValueError("Filename must end with .txt")

main()