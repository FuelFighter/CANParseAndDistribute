import time 
import random as r
import posixpath as pp

folder = 'Logs/'
fileformat = '.txt'


class motorLogger():
	LOGGING = False
	labelString = ('{0:>5s}: {1:>5s}: {2:>5s}: {3:>5s}:').format('mAmp','RPM','Throt','Temp')

	def __init__(self, title):
		self.title = '-' + title
		self.currentTime = ''

	def newLog(self):
		if self.LOGGING == False:
			newTime = time.strftime('%Y-%m-%dT%H-%M-%S')
			if newTime == self.currentTime:
				newTime = newTime + '-2'
			self.currentTime = newTime
			self.titlestring = self.currentTime + self.title
			self.currentFile = folder + self.titlestring + fileformat

			
			self.log = open(self.currentFile, 'w')
			self.log.write(self.titlestring + '\n')
			self.log.write(self.labelString + '\n')
			self.log.close()
			self.LOGGING = True
		else:
			pass
	
	def write(self, Motor):
		if self.LOGGING:
			self.log = open(self.currentFile, 'a')
			newLine = ('{0:5d}, {1:5d}, {2:5d}, {3:5d}\n').format(Motor.Current,Motor.RPM,Motor.Throttle,Motor.Temp)
			self.log.write(newLine)
			self.log.close()
		else:
			pass

	def stop(self):
		self.LOGGING = False
		self.log = open(self.currentFile, 'a')
		newLine = time.strftime('%Y-%m-%dT%H-%M-%S')
		self.log.write(newLine)
		self.log.close()


class batteryLogger():
	LOGGING = False
	labelString = ('{0:>5s}: {1:>5s}: {2:>5s}: {3:>5s}: {4:>5s}: {5:>5s}:').format('mAmp','cVolt','oVolt','temp','state','error')

	def __init__(self, title):
		self.title = '-' + title
		self.currentTime = ''

	def newLog(self):
		if self.LOGGING == False:
			newTime = time.strftime('%Y-%m-%dT%H-%M-%S')
			if newTime == self.currentTime:
				newTime = newTime + '-2'
			self.currentTime = newTime
			self.titlestring = self.currentTime + self.title
			self.currentFile = folder + self.titlestring + fileformat
			self.log = open(self.currentFile, 'w')
			self.log.write(self.titlestring + '\n')
			self.log.write(self.labelString + '\n')
			self.log.close()
			self.LOGGING = True
		else:
			pass
	
	def write(self, Battery, error):
		if self.LOGGING:
			
			cellVoltage = int(Battery.Stack_Voltage/10)
			outVoltage = Battery.Voltage

			Temp = 0
			for cTemp in Battery.Cell_Temp:
				if cTemp > Temp:
					Temp = cTemp

			self.log = open(self.currentFile, 'a')
			newLine = ('{0:>5d}, {1:>5d}, {2:>5d}, {3:>5d}, {4:>5s}, {5:>5s}\n').format(Battery.Current,cellVoltage,outVoltage,Temp,Battery.State,error)
			self.log.write(newLine)
			self.log.close()
		else:
			pass

	def stop(self):
		self.LOGGING = False
		self.log = open(self.currentFile, 'a')
		newLine = time.strftime('%Y-%m-%dT%H-%M-%S')
		self.log.write(newLine)
		self.log.close()


class carLogger():
	LOGGING = False
	labelString = ('{0:>5s}: {1:>5s}:').format('vel','acl')

	def __init__(self, title):
		self.title = '-' + title
		self.currentTime = ''

	def newLog(self):
		if self.LOGGING == False:
			newTime = time.strftime('%Y-%m-%dT%H-%M-%S')
			if newTime == self.currentTime:
				newTime = newTime + '-2'
			self.currentTime = newTime
			self.titlestring = self.currentTime + self.title
			self.currentFile = folder + self.titlestring + fileformat
			self.log = open(self.currentFile, 'w')
			self.log.write(self.titlestring + '\n')
			self.log.write(self.labelString + '\n')
			self.log.close()
			self.LOGGING = True
		else:
			pass
	
	def write(self, Car):
		if self.LOGGING:
			self.log = open(self.currentFile, 'a')
			newLine = ('{0:5d}, {1:5d}\n').format(Car.Velocity,Car.Acceleration)
			self.log.write(newLine)
			self.log.close()
		else:
			pass

	def stop(self):
		self.LOGGING = False
		self.log = open(self.currentFile, 'a')
		newLine = time.strftime('%Y-%m-%dT%H-%M-%S')
		self.log.write(newLine)
		self.log.close()
