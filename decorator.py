#!/usr/bin/python

class Files:
	def __init__(self,**kwargs):
		self.properties = kwargs

	def copy(self):
		print ("Copying")

	def move(self):
		print ("Moving")

	def remove(self):
		print ("Removing")

	def get_properties(self):
		return self.properties

	def get_property(self,key):
		return self.properties.get(key, None)

	@property
	def privacy(self):
		return self.properties.get("privacy", None)

	@privacy.setter
	def privacy(self,c):
		self.properties['privacy']=c

	@privacy.deleter
	def privacy(self):
		del self.properties['privacy']

def main():

	imageDoc = Files()
	imageDoc.privacy="archive"
	print (imageDoc.privacy)

main()