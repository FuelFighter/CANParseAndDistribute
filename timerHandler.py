from time import *


class timer():
	timestamp = 0
	refreshtime = 0
	def __init__(self, time):
		if time != 0:
			self.refreshtime = time
			self.timestamp = time()
		else:
			print('Got no time delay')

	def runOut(self):
		if(time() >= self.timestamp + self.refreshtime):
			self.timestamp = time()
			return True
		else:
			return False

	def reset(self):
		self.timestamp = time()