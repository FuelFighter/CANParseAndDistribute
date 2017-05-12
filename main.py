import serial as ser
from data import CANID, updateCarValues
from serialHandler import SerialModule
from car import Car_c
from time import sleep
from gui import Gui


def sendToTelemetry(Car):
	#write out the values you want to send to the telemetry viewer, 
	#single values and comma seperated.

	output = str(Car.Motor1.RPM) + "," + str(Car.Motor2.RPM)
	output = output + "\n"
	return str.encode(output)

def main():

	Car = Car_c()
	Conn = SerialModule()
	if Conn.MODE == 'CAR':
		UI = Gui()
	
	while(1):
		line = Conn.read()
		if line != '':
			status = updateCarValues(line, Car)
			if status != '':
				print(status)

		if Conn.MODE == 'CAR':
			UI.updateVals(Car)
			UI.refresh()

if __name__ == '__main__':
	main()