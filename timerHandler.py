import time as t


class timer():
	def __init__(self, time):
		if time != 0:
			self.refreshtime = time
			self.timestamp = t.time()
		else:
			print('Got no time delay')

	def runOut(self):
		if(t.time() >= self.timestamp + self.refreshtime):
			self.timestamp = t.time()
			return True
		else:
			return False

	def reset(self):
		self.timestamp = t.time()