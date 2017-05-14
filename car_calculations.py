import timerHandler


TIRE_DIAMETER = 0.55
RPM_TO_METER_P_SECOND = TIRE_DIAMETER * 3.14159 / 60

def calculateVelocity(RPM):
	return RPM*RPM_TO_METER_P_SECOND

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
		errorString = 'Nothing to worry about'

	return errorString


class multiClick():
	clicks = 0
	threshold = 0
	triggered = False
	pressed = False
	def __init__(self, threshold, timeout):
		self.threshold = threshold
		self.clickTimer = timer(timeout)

	def pressed(self):
		if (self.pressed == False) && (self.clicks == 0):
			self.clickTimer.reset()
		if (self.pressed == False) && (self.clickTimer.runOut() == False):
			self.clicks = self.clicks + 1
			self.pressed = True
		if self.clicks == self.threshold:
			self.triggered = True

	def released(self):	
		if (self.pressed == True):
			self.pressed = False

	def state(self):
		state = self.triggered
		self.triggered = False
		self.clicks = 0
		return state




