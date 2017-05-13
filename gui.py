import tkinter as tk
import time as t
from car_calculations import *

class guiVariableLabel():
	def __init__(self, master, text, suffix, row, column, sticky, varFont, labFont):
		self.label = tk.Label(master, text=text, font=labFont, bg='white',fg='#222F63')
		self.label.grid(row=row,column=column,sticky=sticky)
		self.variable = tk.StringVar()
		self.variablelabel = tk.Label(master, textvariable=self.variable,width=6,font=varFont, bg='white', fg='#222F63')
		self.variablelabel.grid(row=row,column=column+1,sticky='w')
		self.suffixlabel = tk.Label(master, text=suffix,width=5,font=labFont, bg='white', fg='#222F63')
		self.suffixlabel.grid(row=row,column=column+2,sticky='nsw')

	def setVar(self, text):
		self.variable.set(text)

class guiStateLabel():
	def __init__(self, master, text, row, column, sticky, varFont, labFont):
		self.label = tk.Label(master, text=text, font=labFont, fg='#222F63', bg='white')
		self.label.grid(row=row,column=column,sticky=sticky)
		self.variable = tk.StringVar()
		self.variablelabel = tk.Label(master, textvariable=self.variable, width=12, font=varFont, bg='white', fg='#222F63')
		self.variablelabel.grid(row=row,column=column+1,sticky='w')

	def setVar(self, text):
		self.variable.set(text)


class guiMotor():
	def __init__(self, master, number, row, column, sticky, varFont, labFont):
		self.frame = tk.Frame(master, bg='white')
		self.frame.grid(row=row,column=column,sticky=sticky,ipadx=2,ipady=2)
		self.label = tk.Label(self.frame,text="Motor " + str(number) + ":",font=labFont, bg='white', fg='#222F63')
		self.label.grid(row=0,column=0,sticky='e')

		self.throttle = guiVariableLabel(self.frame, 'Throttle:', '%', 1, 0, 'e', varFont, labFont)
		self.current = guiVariableLabel(self.frame, 'Current:', 'mA', 2, 0, 'e', varFont, labFont)
		self.rpm = guiVariableLabel(self.frame, 'RPM:', '', 3, 0, 'e', varFont, labFont)

	def setThrottle(self, value):
		self.throttle.setVar(str(value))

	def setCurrent(self, value):
		self.current.setVar(str(value))

	def setRPM(self,value):
		self.rpm.setVar(str(value))

class guiBattery():
	def __init__(self, master, row, column, sticky, varFont, labFont):
		self.frame = tk.Frame(master,bg='white')
		self.frame.grid(row=row,column=column,sticky=sticky,ipadx=2,ipady=2)
		self.label = tk.Label(self.frame, text="Battery:", font=labFont, fg='#222F63',bg='white')
		self.label.grid(row=0,column=0,sticky='e')

		self.voltage = guiVariableLabel(self.frame, 'Voltage:', 'V', 3, 0, 'e', varFont, labFont)
		self.current = guiVariableLabel(self.frame, 'Current:', 'A', 2, 0, 'e', varFont, labFont)
		#self.errorFlag = guiStateLabel(self.frame, 'Error:', 4, 0, 'e', varFont, labFont)
		self.state = guiStateLabel(self.frame, 'State:', 1, 0, 'e', varFont, labFont)

	def setVoltage(self, value):
		self.voltage.setVar(format(value,'.2f'))

	def setCurrent(self, value):
		self.current.setVar(format(value,'.2f'))

	def setState(self, value):	
		self.state.setVar(value)


class guiMainWindowVariable():

	def __init__(self, master, text, suffix, row, column, sticky, varFont, labFont):
		self.label = tk.Label(master, text=text, font=labFont, fg='#222F63',bg='white')
		self.label.grid(row=row,column=column,sticky=sticky)
		self.variable = tk.StringVar()
		self.variablelabel = tk.Label(master, textvariable=self.variable, font=varFont, fg='#222F63',bg='white')
		self.variablelabel.grid(row=row+1,column=column,sticky='e')
		self.suffixlabel = tk.Label(master, text=suffix,width=5,font=labFont,fg='#222F63',bg='white')
		self.suffixlabel.grid(row=row+1,column=column+1,sticky='w')

	def setVar(self, text):
		self.variable.set(text)

		
class Gui():
	
	largeFontBold = ("Arial",70,'bold')
	mediumFont = ("Arial",24)
	smallFont = ("Arial",14)
	smallFontBold = ("Arial",14,'bold')

	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry('800x480')
		self.root.wm_attributes('-fullscreen','true')
		self.root.config(bg='#222F63')

		self.mainFrame = tk.Frame(self.root)
		self.mainFrame.config(bg='white')
		self.mainFrame.pack(side='top',padx=5,pady=5)

		self.infoFrame = tk.Frame(self.root)
		self.infoFrame.config(bg='#222F63')
		self.infoFrame.pack(side='top',padx=5,pady=5)

		self.errorFrame = tk.Frame(self.root)
		self.errorFrame.config(bg='#222F63')
		self.errorFrame.pack(side='top',padx=5,pady=5)

		self.Velocity = guiMainWindowVariable(self.mainFrame, 'Velocity:', 'km/h', 0, 0, 'w', self.largeFontBold, self.mediumFont)
		#self.AvgVel = guiMainWindowVariable(self.mainFrame, 'Average Vel:','km/h', 0, 2, 'w', self.largeFontBold, self.mediumFont)
		#self.Time = guiMainWindowVariable(self.mainFrame, 'Elapsed Time:','min', 2, 0, 'w', self.largeFontBold, self.mediumFont)

		self.Motor1 = guiMotor(self.infoFrame, 1, 1, 0, 'w', self.smallFontBold, self.smallFont)
		self.Motor2 = guiMotor(self.infoFrame, 2, 1, 1, 'w', self.smallFontBold, self.smallFont)
		self.Battery = guiBattery(self.infoFrame, 1, 2, 'w', self.smallFontBold, self.smallFont)

		self.ErrorVar = guiStateLabel(self.errorFrame, 'Battery Error: ', 0, 0, 'w', self.smallFont, self.smallFontBold)


	def refresh(self):
		self.root.update_idletasks() 
		self.root.update()

	def updateVals(self, Car):
		self.Velocity = calculateKmh(Car.Velocity)
		#self.AvgVel = Car.AvgVel

		self.Motor1.setThrottle(Car.Motor1.Throttle)
		self.Motor1.setCurrent(Car.Motor1.Current)
		self.Motor1.setRPM(Car.Motor1.RPM)

		self.Motor2.setThrottle(Car.Motor2.Throttle)
		self.Motor2.setCurrent(Car.Motor2.Current)
		self.Motor2.setRPM(Car.Motor2.RPM)

		self.Battery.setVoltage(Car.Battery.Voltage/1000)
		self.Battery.setCurrent(Car.Battery.Current/1000)
		self.Battery.setState(Car.Battery.State)


		errorString = createErrorString(Car)

		length = len(errorString)
		self.ErrorVar.variablelabel.config(width=length)
		self.ErrorVar.setVar(errorString)