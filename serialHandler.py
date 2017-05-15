import serial as ser
import sys
import os
import time as t

class SerialModule():

	CAN_COMPORT = 'COM7'
	CAN_BAUD = '500000'

	TELE_COMPORT = 'COM24'
	TELE_BAUD = '460800'

	BYPASS_COMPORT = 'COM26'
	BYPASS_BAUD = '460800'

	MODE = "CAR"

	NEW_LINE = False
	STRING_BUFFER = ''

	def __init__(self):
		asking = True
		print('Starting Serial Parser')
		print(('Connection information: CanSerial({}:{}), TelemetrySerial({}:{}) and ByPassSerial({}:{})').format(self.CAN_COMPORT, self.CAN_BAUD, self.TELE_COMPORT, self.TELE_BAUD, self.BYPASS_COMPORT, self.BYPASS_BAUD))
		print('You may change the Comports and Baudrates in the serialHandler.py')
		print(('Running {} config..').format(self.MODE))

		if self.MODE == 'CAR':
			try:
				self.canSerial = ser.Serial(self.CAN_COMPORT,self.CAN_BAUD)
				print(('Connected to CanSerial({}:{})').format(self.CAN_COMPORT,self.CAN_BAUD))

			except KeyboardInterrupt:
				self.close()

		elif self.MODE == 'LAPTOP':
			try:
				self.byPassSerial = ser.Serial(self.BYPASS_COMPORT,self.BYPASS_BAUD)
				self.canSerial = ser.Serial(self.CAN_COMPORT,self.CAN_BAUD)
				self.teleSerial = ser.Serial(self.TELE_COMPORT,self.TELE_BAUD)
				print(('Connected to CanSerial({}:{}), TelemetrySerial({}:{}) and ByPassSerial({}:{})').format(self.CAN_COMPORT, self.CAN_BAUD, self.TELE_COMPORT, self.TELE_BAUD, self.BYPASS_COMPORT, self.BYPASS_BAUD))	
			except KeyboardInterrupt:
				self.close()
		else:
			sys.exit()

	def read(self):

			if self.NEW_LINE == True:
				self.STRING_BUFFER = ''
				self.NEW_LINE = False

			while(self.canSerial.inWaiting()>0) & (self.NEW_LINE == False):
				data = self.canSerial.read()
				self.STRING_BUFFER = self.STRING_BUFFER + data.decode('ascii')
				if ']' in self.STRING_BUFFER:
					self.NEW_LINE = True
					break

			if (self.MODE == 'CAR') & (self.NEW_LINE == True):
				return self.STRING_BUFFER

			elif (self.MODE == 'LAPTOP') & (self.NEW_LINE == True):
				self.byPassSerial.write(str.encode(self.STRING_BUFFER))
				return self.STRING_BUFFER

			else:
				return ''

	def send(self, string):
		self.teleSerial.write(str.encode(string))

	def close(self):
		if self.MODE == 'CAR':
			self.canSerial.close()
		elif self.MODE == 'LAPTOP':
			self.canSerial.close()
			self.byPassSerial.close()
			self.teleSerial.close()
		print('Closing') 	