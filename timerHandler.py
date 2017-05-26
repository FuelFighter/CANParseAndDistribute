import time as t


class timer():
	enabled = False
	timestamp = 0
	def __init__(self, time):
		if time != 0:
			self.refreshtime = time
		else:
			print('Got no time delay')

	def timeout(self):
		if self.enabled:
			if(t.time() > self.timestamp + self.refreshtime):
				return True
		return False

	def stop(self):
		self.enabled = False
		
	def start(self):
		self.enabled = True
		self.timestamp = t.time()