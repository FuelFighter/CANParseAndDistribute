import timerHandler as t
import time as time
import math

TIRE_DIAMETER = 0.55
RPM_TO_METER_P_SECOND = (TIRE_DIAMETER * 3.14159) / 60
TARGET_LAP_TIME_s = 10


class multiClick():
	clicks = 0
	threshold = 0
	pressed = False
	def __init__(self, threshold, timeout):
		self.threshold = threshold
		self.timer = t.timer(timeout)

	def press(self):
		if (not self.pressed) & (not self.timer.enabled):
			self.timer.start()
			self.pressed = True
			self.clicks = 1
			print('Press')
		elif (not self.pressed): #& (not self.timer.timeout()):
			self.pressed = True
			self.clicks = self.clicks + 1
			print('Press')


	def release(self):	
		if (self.pressed == True):
			self.pressed = False

	def state(self):
		if (self.clicks == self.threshold) & (self.timer.timeout()):
			self.clicks = 0
			self.timer.stop()
			return True
		if self.timer.timeout():
			self.clicks = 0
			self.timer.stop()
		return False


class lapTimer():
	startup_time = 0
	lap_times = [0.0]*13
	lap_timestamps = [0.0]*13
	formated_lap_times = ['']*13
	lap_index = 0

	def __init__(self):
		self.startup_time = time.time()

	def updateTimer(self):
		self.current_time = time.time()
		if self.lap_index == 0:
			self.lap_times[self.lap_index] = self.current_time - self.startup_time
		elif self.lap_index > 11:
			self.lap_times[self.lap_index] = self.current_time - self.lap_timestamps[11]
		else: 
			self.lap_times[self.lap_index] = self.current_time - self.lap_timestamps[self.lap_index-1]

		self.lap_timestamps[self.lap_index] = self.current_time
		self.formated_lap_times[self.lap_index] = self.formatSeconds(self.lap_times[self.lap_index])

	def formatSeconds(self, seconds):
		seconds = int(math.ceil(seconds))
		m, s = divmod(seconds, 60)

		
		time_string = ('%02dm:%02ds') % (m, s)

		return time_string

	def newLap(self):
		self.updateTimer()
		if self.lap_index > 11:
			print(self.lap_index)
			return
		self.lap_index = self.lap_index + 1
		print(self.lap_index)	
		print(self.avgLapTime())


	def currentLapTime(self):
		if self.lap_index > 11:
			return self.formatSeconds(self.lap_times[11])
		return self.formatSeconds(self.lap_times[self.lap_index])

	def avgLapTime(self):
		if self.lap_index == 0:
			avgTime = 0
		elif self.lap_index == 1: 
			avgTime = 0
		elif self.lap_index == 2:
			avgTime = self.lap_times[1]
		else:
			tot_time = 0.0
			for lapTime in self.lap_times[1:(self.lap_index-1)]:
				tot_time = tot_time + math.ceil(lapTime)

			avgTime = ((tot_time * 1000)/(self.lap_index-1))/1000

		return math.ceil(avgTime)

	def validLapTIme(self, lap_time):
		if lap_time >= TARGET_LAP_TIME_s:
			return '#FF0000'
		elif lap_time < TARGET_LAP_TIME_s:
			return '#5CCB76'

	def totalTime(self):
		self.current_time = time.time()
		if self.lap_index == 0:
			tot_time = self.current_time - self.startup_time
		else:
			tot_time = self.current_time - self.lap_timestamps[self.lap_index - 1]
		return self.formatSeconds(tot_time)


def calculateVelocity(RPM):
	velocity = RPM*RPM_TO_METER_P_SECOND
	if velocity > 50.0:
		velocity = 0
	return velocity

def calculateKmh(velocity):
	return velocity*3.6

def createBatteryErrorString(Car):
	errorString = ''

	if Car.Battery.Error_PreChargeTimeout == True:
		errorString = 'PreChargeTimeout'

	if Car.Battery.Error_LTC_LossOfSignal == True:
		if errorString != '':
			errorString = errorString + ', ' 
		errorString = errorString + 'LTC_LossOfSignal'

	if Car.Battery.Error_OverVoltage == True:
		if errorString != '':
			errorString = errorString + ', '
		errorString = errorString + 'OverVoltage'

	if Car.Battery.Error_UnderVoltage == True:
		if errorString != '':
			errorString = errorString + ', '
		errorString = errorString + 'UnderVoltage'

	if Car.Battery.Error_OverCurrent == True:
		if errorString != '':
			errorString = errorString + ', '
		errorString = errorString + 'OverCurrent'

	if Car.Battery.Error_OverTemp == True:
		if errorString != '':
			errorString = errorString + ', '
		errorString = errorString + 'OverTemp'

	if Car.Battery.Error_NoDataOnStartup == True:
		if errorString != '':
			errorString = errorString + ', '
		errorString = errorString + 'NoDataOnStartup'

	if errorString == '':
		errorString = 'Ok'

	return errorString

def calculateStackVoltage(Car):
	Car.Battery.Stack_Voltage = 0
	for cVolt in Car.Battery.Cell_Voltage:
		Car.Battery.Stack_Voltage = Car.Battery.Stack_Voltage + cVolt

def createLoggingString(Car):
	logstring = ''

	if Car.log.LOGGING:
		logstring = 'Car, '
	if Car.Motor1.log.LOGGING:
		logstring = logstring + 'Motor1, '
	if Car.Motor2.log.LOGGING:
		logstring = logstring + 'Motor2, '
	if Car.Battery.log.LOGGING:
		logstring = logstring + 'Battery '
	if logstring == '':
		logstring = 'No'
	return logstring


def runCalculations(Car):
	calculateStackVoltage(Car)





