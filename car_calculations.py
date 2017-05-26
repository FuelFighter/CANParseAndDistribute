import timerHandler as t


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





