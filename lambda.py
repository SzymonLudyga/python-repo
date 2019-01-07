import operator

def calc(x):

	return (x*2)

print (calc(3))

t = lambda x,y: (x*y,x+y) 

print (t(7,6)[1])

getseconditem = operator.itemgetter(2)

ls = ['a','b','c']

print (getseconditem(ls))

print (operator.itemgetter(1,2,5)('dajfgahfja'))