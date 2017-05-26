import timerHandler as t
import time as time
import math

TIRE_DIAMETER = 0.55
RPM_TO_METER_P_SECOND = (TIRE_DIAMETER * 3.14159) / 60


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
	lap_times = [0.0]*12
	lap_timestamps = [0.0]*12
	formated_lap_times = ['']*12
	lap_index = 0

	def __init__(self):
		self.startup_time = time.time()

	def updateTimer(self):
		if self.lap_index >= 9:
			return

		self.current_time = time.time()
		if self.lap_index == 0:
			self.lap_times[self.lap_index] = self.current_time - self.startup_time
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
		if self.lap_index >= 15:
			return
		self.updateTimer()
		self.lap_index = self.lap_index + 1


	def currentLapTime(self):
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
				tot_time = tot_time + lapTime
			print(tot_time)
			tot_time = math.ceil(tot_time)
			print(str(tot_time) + ' / ' + str(self.lap_index-1))
			avgTime = tot_time/(self.lap_index)
			print('= ' + str(avgTime))

		return self.formatSeconds(avgTime)

	def totalTime(self):
		self.current_time = time.time()
		return self.formatSeconds(self.current_time - self.startup_time)


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





