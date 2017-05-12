import serial as ser
from data import CANID, updateCarValues
from serialHandler import SerialModule
from car import Car_c
from time import *
from gui import Gui
from refreshHandler import *




def main():
	guiRefreshTimer = timer(10)
	Car = Car_c()
	#Conn = SerialModule()
	#if Conn.MODE == 'CAR':
	UI = Gui()
	
	teller = 0

	while(1):
		line = ""
		#line = Conn.read()
		if line != '':
			status = updateCarValues(line, Car)
			if status != '':
				print(status)
		if (guiRefreshTimer.refresh()):
			
			
			teller = teller + 1
			if (teller > 1000):
				teller = 0
			print(teller)
			#status = updateCarValues("[1C2:3:AABBCC]", Car)
			UI.updateVals(Car)
			UI.refresh()
			UI.updateVals(Car)
			UI.refresh()
			UI.updateVals(Car)
			UI.refresh()
			UI.updateVals(Car)
			UI.refresh()
			UI.updateVals(Car)
			UI.refresh()
		print("ASDKFJKADF")

if __name__ == '__main__':
	main()