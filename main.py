import serial as ser
from data import CANID, updateCarValues
from serialHandler import SerialModule
from Car import Car_c
from time import sleep
from gui import Gui
import random as random
import car_calculations as cc
import timerHandler as th
import sys

def main():

	Car = Car_c()
	Conn = SerialModule()

	UIRefreshTimer = th.timer(0.1)
	UIRefreshTimer.start()

	if Conn.MODE == 'CAR':
		UI = Gui()
	ceiling = random.random()*150
	count = 0
	while(1):

		try:
			timerState = UIRefreshTimer.timeout()
			if timerState:
				count = count + 1
				UI.lapHandler.updateTimer()
				UIRefreshTimer.start()

			line = Conn.read()
			if line != '':
				try:
					status = updateCarValues(line, Car)
					if status != '':
						print(status)
				except:
					pass

			if count >= ceiling:
				UI.lapHandler.newLap()
				ceiling = random.random()*150
				count = 0

			if timerState:
				cc.runCalculations(Car)
				Conn.send(Car)
				if Conn.MODE == 'CAR':
					UI.updateVals(Car)
					UI.refresh()

			if Car.Interface.LapClick.state():
				if not Car.log.LOGGING:
					Car.log.newLog()
					Car.Motor1.log.newLog()
					Car.Motor2.log.newLog()
					Car.Battery.log.newLog()
				elif Car.log.LOGGING:
					Car.log.stop()
					Car.Motor1.log.stop()
					Car.Motor2.log.stop()
					Car.Battery.log.stop()

					Car.log.newLog()
					Car.Motor1.log.newLog()
					Car.Motor2.log.newLog()
					Car.Battery.log.newLog()
				UI.lapHandler.newLap()



			if Car.log.LOGGING & timerState:
				Car.log.write(Car)
				Car.Motor1.log.write(Car.Motor1)
				Car.Motor2.log.write(Car.Motor2)
				Car.Battery.log.write(Car.Battery,cc.createBatteryErrorString(Car))

		except KeyboardInterrupt:
			sys.exit()


if __name__ == '__main__':
	main()