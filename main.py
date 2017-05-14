import serial as ser
from data import CANID, updateCarValues
from serialHandler import SerialModule
from car import Car_c
from time import sleep
from gui import Gui
import timerHandler


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
		UIRefreshTimer = timer()
	
	while(1):

		timerState = UIRefreshTimer.runOut()

		line = Conn.read()
		if line != '':
			status = updateCarValues(line, Car)
			if status != '':
				print(status)

		if timerState:
			runCalculations(Car)

		if Car.Interface.LapDoubleClick.triggered():
			if not Car.log.LOGGING:
				Car.log.newLog()
				Car.Motor1.log.newLog()
				Car.Motor2.log.newLog()
				Car.Battery.log.newLog()
			else if Car.log.LOGGING:
				Car.log.stop()
				Car.Motor1.log.stop()
				Car.Motor2.log.stop()
				Car.Battery.log.stop()

		if Car.log.LOGGING && timerState:
			Car.log.write(Car)
			Car.Motor1.log.write(Car.Motor1)
			Car.Motor2.log.write(Car.Motor2)
			Car.Battery.log.write(Car.Battery,createBatteryErrorString(Car)

		if Conn.MODE == 'CAR' && timerState:
			UI.updateVals(Car)
			UI.refresh()


if __name__ == '__main__':
	main()