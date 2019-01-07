class InclusiveRange:

	def __init__(self,*args):
		numargs=len(args)
		if numargs < 1: raise TypeError ('requires at least 1 parameter')
		elif numargs == 1:
			self.stop=args[0]
			self.step=1
			self.start=0
		elif numargs == 2:
			(self.start,self.stop)= args
			self.step=1
		elif numargs == 3:
			(self.start,self.stop,self.step) = args
		else:
			raise TypeError('Received {} param'.format(numargs))

	def __iter__(self):
		i = self.start
		while i <= self.stop:
			yield i 
			i += self.step

def main():

	o = InclusiveRange(10,100,3)
	for i in o: print (i,end=' ')
	print()

main()