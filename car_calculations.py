import timerHandler as t


TIRE_DIAMETER = 0.55
RPM_TO_METER_P_SECOND = TIRE_DIAMETER * 3.14159 / 60


class multiClick():
	clicks = 0
	threshold = 0
	triggered = False
	pressed = False
	def __init__(self, threshold, timeout):
		self.threshold = threshold
		self.clickTimer = t.timer(timeout)

	def press(self):
		if (self.pressed == False) & (self.clicks == 0):
			self.clickTimer.reset()
		if (self.pressed == False) & (self.clickTimer.runOut() == False):
			self.clicks = self.clicks + 1
			self.pressed = True
		if self.clicks == self.threshold:
			self.triggered = True

	def release(self):	
		if (self.pressed == True):
			self.pressed = False

	def state(self):
		state = self.triggered
		self.triggered = False
		self.clicks = 0
		return state

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
		errorString = 'No Error'

	return errorString

def calculateStackVoltage(Car):
	for cVolt in Car.Battery.Cell_Voltage[0:5]:
		Car.Battery.Stack_Voltage[0] = Car.Battery.Stack_Voltage[0] + cVolt
	for cVolt in Car.Battery.Cell_Voltage[6:11]:
		Car.Battery.Stack_Voltage[1] = Car.Battery.Stack_Voltage[1] + cVolt

def runCalculations(Car):
	calculateStackVoltage(Car)





