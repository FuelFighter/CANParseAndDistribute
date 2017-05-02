import serial as ser
from parseData import CANID, parseCANString
from Car import Car_c
from time import sleep
import sys
import os

TIRE_DIAMETER = 0.55
RPM_TO_METER_P_SECOND = TIRE_DIAMETER * 3.14159 / 60
SAMPLERATE = 0.1

def sendToTelemetry(Car):
	#write out the values you want to send to the telemetry viewer, 
	#single values and comma seperated.

	output = str(Car.Motor1.RPM) + "," + str(Car.Motor2.RPM)
	output = output + "\n"
	return str.encode(output)

def updateCarValues(Car, ID, Data):
	if ID == CANID['Brake']:
		if int('0x' + Data[0],16) == 1:
			Car.Brake = True
		else:
			Car.Brake = False

	elif ID == CANID['Encoder']:
		Car.Motor1.RPM = int('0x' + Data[0] + Data[1], 16)
		Car.Motor2.RPM = int('0x' + Data[2] + Data[3], 16)
		Car.RPM = int('0x' + Data[4] + Data[5], 16)
		Car.Torque = int('0x' + Data[6] + Data[7], 16)

		OldVelocity = Car.Velocity
		Car.Velocity = Car.RPM * RPM_TO_METER_P_SECOND
		Car.Acceleration = (Car.Velocity - OldVelocity)/SAMPLERATE

	elif ID == CANID['Steering Wheel']:
		Car.Throttle = int('0x' + Data[3], 16)
		throttleLeft = int('0x' + Data[2], 16)
		
		if throttleLeft > 50:
			Car.Deadmanswitch = True
		else:
			Car.Deadmanswitch = False
		 
	elif ID == CANID['Dashboard']:
		pass
	elif ID == CANID['BMS Cell V 1-4']:
		pass
	elif ID == CANID['BMS Cell V 5-7']:
		pass
	elif ID == CANID['BMS Cell V 8-12']:
		pass
	elif ID == CANID['BMS Cell Temp']:	
		pass
	elif ID == CANID['BMS Volt Current']:
		pass
	elif ID == CANID['BMS Status']:
		pass
	elif ID == CANID['BMS Error Flags']:
		pass
	elif ID == CANID['Motor 1 Status']:
		Car.Motor1.Current = int('0x' + Data[1] + Data[2], 16)
		Car.Motor1.Current = int('0x' + Data[3] + Data[4], 16)
		Car.Motor1.Throttle = int('0x' + Data[5], 16)

	elif ID == CANID['Motor 2 Status']:
		Car.Motor2.Current = int('0x' + Data[1] + Data[2], 16)
		Car.Motor2.Current = int('0x' + Data[3] + Data[4], 16)
		Car.Motor2.Throttle = int('0x' + Data[5], 16)

	elif ID == CANID['Front Lights Status']:
		pass
	else:
		pass

def main():

	asking = True
	print('Starting Serial Parser')
	CAN_COMPORT = 'COM19'
	TELE_COMPORT = 'COM21'
	BYPASS_COMPORT = 'COM23'
	print(('I have {} as your CANViewer COMPORT, {} as your Telemetry COMPORT and {} as your bypass COMPORT. Is this correct? Y/N').format(CAN_COMPORT,TELE_COMPORT,BYPASS_COMPORT))
	prompt = input()
	if (prompt == "Y") or (prompt == 'y'):
		asking = False

	while(asking):
		print('Enter the COM-port of the CANViewer UM:')
		CAN_COMPORT = input()
		print('Enter the COM-port of the telemetry viewer:')
		TELE_COMPORT = input()
		print('Enter the COM-port of the bypass COMPORT:')
		BYPASS_COMPORT = input()
		print(('You entered {} as your CANViewer COMPORT, {} as your Telemetry COMPORT and {} as your bypass COMPORT. Is this correct? Y/N').format(CAN_COMPORT,TELE_COMPORT,BYPASS_COMPORT))
		prompt = input()
		if prompt == "Y":
			asking = False
	print("Allright, lets handle som data!")
	print("Running.. ")	

	Car = Car_c()
	line = ""

	byPassSerial = ser.Serial(BYPASS_COMPORT,'460800')
	canSerial = ser.Serial(CAN_COMPORT,'250000')
	teleSerial = ser.Serial(TELE_COMPORT,'460800')	

	while(1):
		try:		
			if canSerial.inWaiting()>0:
				line = canSerial.readline()
				byPassSerial.write(line)
				line = line.decode('ascii')

				ID, Data = parseCANString(line)
				updateCarValues(Car, ID, Data)
			
			teleSerial.write(sendToTelemetry(Car))
			sleep(0.1)

		except KeyboardInterrupt:
			byPassSerial.close()
			canSerial.close()
			teleSerial.close()
			print('Closing..')
			try:
				sys.exit(0)
			except SystemExit:
				os._exit(0)		

		line = ""



if __name__ == '__main__':
	main()