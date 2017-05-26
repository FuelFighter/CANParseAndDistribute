import serial as ser
import sys
import os
import time as t
import car_client as tcp
import car_calculations

class SerialModule():

	CAN_COMPORT = 'COM23'
	CAN_BAUD = '500000'

	TELE2_COMPORT = 'COM22'
	TELE2_BAUD = '460800'

	BYPASS_COMPORT = 'COM26'
	BYPASS_BAUD = '460800'

	MODE = "CAR"

	NEW_LINE = False
	STRING_BUFFER = ''

	def __init__(self):
		asking = True
		print('Starting Serial Parser')
		print(('Connection information: CanSerial({}:{}), TelemetrySerial({}:{}) and ByPassSerial({}:{})').format(self.CAN_COMPORT, self.CAN_BAUD, self.TELE2_COMPORT, self.TELE2_BAUD, self.BYPASS_COMPORT, self.BYPASS_BAUD))
		print('You may change the Comports and Baudrates in the serialHandler.py')
		print(('Running {} config..').format(self.MODE))
		
		self.TCPConn = tcp.Client("37.187.53.31", 800)

		if self.MODE == 'CAR':
			try:
				self.canSerial = ser.Serial(self.CAN_COMPORT,self.CAN_BAUD)
				print(('Connected to CanSerial({}:{})').format(self.CAN_COMPORT,self.CAN_BAUD))

			except KeyboardInterrupt:
				self.close()

		elif self.MODE == 'LAPTOP':
			try:
				self.byPassSerial = ser.Serial(self.BYPASS_COMPORT,self.BYPASS_BAUD)
				#self.tele1Serial = ser.Serial(self.TELE1_COMPORT,self.TELE1_BAUD)
				self.tele2Serial = ser.Serial(self.TELE2_COMPORT,self.TELE2_BAUD)
				print(('Connected to CanSerial({}:{}), TelemetrySerial({}:{}) and ByPassSerial({}:{})').format(self.CAN_COMPORT, self.CAN_BAUD, self.TELE2_COMPORT, self.TELE2_BAUD, self.BYPASS_COMPORT, self.BYPASS_BAUD))	
			except KeyboardInterrupt:
				self.close()
		else:
			sys.exit()

	def read(self):

			if self.NEW_LINE == True:
				self.STRING_BUFFER = ''
				self.NEW_LINE = False

			if (self.MODE == 'CAR'):
				while(self.canSerial.inWaiting()>0) & (self.NEW_LINE == False):
					data = self.canSerial.read()
					self.STRING_BUFFER = self.STRING_BUFFER + data.decode('ascii')
					if '\n' in self.STRING_BUFFER:
						self.NEW_LINE = True
						print(self.STRING_BUFFER)
						self.TCPConn.send(self.STRING_BUFFER)
						return self.STRING_BUFFER

			elif (self.MODE == 'LAPTOP'):
				data = self.TCPConn.receive()
				if data != '':
					self.STRING_BUFFER = self.STRING_BUFFER + data
				if '\n' in self.STRING_BUFFER:
					self.NEW_LINE = True
					print(self.STRING_BUFFER)
					self.byPassSerial.write(str.encode(self.STRING_BUFFER))
					return self.STRING_BUFFER
			else:
				return ''

	def send(self, Car):
		if self.MODE == 'CAR':
			return

		motor1 = ('{0:>5.3f}, {1:>5d}, {2:>5d}, ').format(Car.Motor1.Current/1000, Car.Motor1.RPM, Car.Motor1.Throttle)
		motor2 = ('{0:>5.3f}, {1:>5d}, {2:>5d}, ').format(Car.Motor1.Current/1000, Car.Motor1.RPM, Car.Motor1.Throttle)		

		cellVoltage = int(Car.Battery.Stack_Voltage/10)
		outVoltage = Car.Battery.Voltage

		Temp = 0
		for cTemp in Car.Battery.Cell_Temp:
			if cTemp > Temp:
				Temp = cTemp

		lowestCVolt = 100000000
		highestCVolt = 0
		for cVolt in Car.Battery.Cell_Voltage:
			if cVolt > highestCVolt:
				highestCVolt = cVolt
			if cVolt < lowestCVolt:
				lowestCVolt = cVolt

		#Current, out Voltage, total cell voltage, lowest cell voltage, highest cell voltage, highest temp
		battery = ('{0:>5.3f}, {1:>5.3f}, {2:>5.3f}, {3:>5.3f}, {4:>5.3f}, {5:>5.3f}\n').format(Car.Battery.Current/1000, outVoltage/1000, cellVoltage/1000, lowestCVolt/10000, highestCVolt/10000, Temp/10)
		self.tele2Serial.write(str.encode(motor1 + motor2 + battery))
		#self.tele1Serial.write(str.encode(battery))

	def close(self):
		if self.MODE == 'CAR':
			self.canSerial.close()
		elif self.MODE == 'LAPTOP':
			self.canSerial.close()
			self.byPassSerial.close()
			self.tele2Serial.close(	)
		print('Closing') 	