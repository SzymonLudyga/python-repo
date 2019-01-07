
seasons = ['spring','summer']

print (list(enumerate(seasons,start=3)))

x=3

print (eval('x*2'))  #  eval('expression')


# iter
with open ("filename1.txt") as fh:
	for line in iter(fh.readline,''):
		print (line)

def main():

	print ("this is a sample generator")
	for i in inclusive_range(0,25,1):
		print (i , end=' ')
	print()

def inclusive_range(start,stop,step):
	i = start
	while i < stop:
		yield i
		i+=step

main()