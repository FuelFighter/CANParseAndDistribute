from time import *




class timer():
	timestamp = 0
	refreshtime = 0
	Hz = 0
	def __init__(self, Hz):
		if(Hz > 0):
			self.Hz = Hz
			self.refreshtime = 1/Hz
			self.timestamp = time()
		else:
			print("Invalid Hz")

	def refresh(self):
		if(time() > self.timestamp + self.refreshtime):
			self.timestamp = time()
			return True
		else:
			return False

