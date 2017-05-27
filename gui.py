import tkinter as tk
import time as time
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
		self.variablelabel.grid(row=row,column=column+1,sticky='n')

	def setVar(self, text):
		self.variable.set(text)
		length = len(text)
		self.variablelabel.config(width=length)

	def setBgColor(self, color):
		self.variablelabel.config(bg=color)

	def setFgColor(self, color):
		self.variablelabel.config(fg=color)


class guiMotor():
	def __init__(self, master, number, row, column, sticky, varFont, labFont):
		self.frame = tk.Frame(master, bg='white')
		self.frame.grid(row=row,column=column,sticky=sticky,ipadx=2,ipady=2)
		self.label = guiStateLabel(self.frame, 'Motor '+ str(number) +':', 0, 0, 'e', varFont, labFont)
		#self.label = tk.Label(self.frame,text="Motor " + str(number) + ":",font=labFont, bg='white', fg='#222F63')
		#self.label.grid(row=0,column=0,sticky='e')

		self.throttle = guiVariableLabel(self.frame, 'Throttle:', '%', 1, 0, 'e', varFont, labFont)
		self.current = guiVariableLabel(self.frame, 'Current:', 'A', 2, 0, 'e', varFont, labFont)
		self.rpm = guiVariableLabel(self.frame, 'RPM:', '', 3, 0, 'e', varFont, labFont)

	def setThrottle(self, value):
		self.throttle.setVar(str(value))

	def setCurrent(self, value):
		self.current.setVar(str(value))

	def setRPM(self,value):
		self.rpm.setVar(str(value))

	def setState(self,value):
		self.label.setVar(value)

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

class guiTimer():
	def __init__(self, master, row, column, sticky, varFont, labFont):
		self.frame = tk.Frame(master,bg='white')
		self.frame.grid(row=row,column=column,sticky=sticky,ipadx=2,ipady=2)

		self.time = guiStateLabel(self.frame, 'Time:', 0, 0, 'e', varFont, labFont)
		self.lapTime = guiStateLabel(self.frame, 'Lap Time:', 1, 0, 'e', varFont, labFont)
		self.avgLapTime = guiStateLabel(self.frame, 'Avg Lap Time:', 2, 0, 'e', varFont, labFont)

	def setTime(self, value):	
		self.time.setVar(value)

	def setLapTime(self, value):	
		self.lapTime.setVar(value)

	def setAvgLapTime(self, value):	
		self.avgLapTime.setVar(value)


class guiLapTimes():
	def __init__(self, master, row, column, sticky, varFont, labFont):
		self.frame = tk.Frame(master,bg='white')
		self.frame.grid(row=row,column=column,sticky=sticky,ipadx=2,ipady=2)

		self.lap0 = guiStateLabel(self.frame, '0:', 1, 0, 'e', varFont, labFont)
		self.lap1 = guiStateLabel(self.frame, '1:', 2, 0, 'e', varFont, labFont)
		self.lap2 = guiStateLabel(self.frame, '2:', 3, 0, 'e', varFont, labFont)
		self.lap3 = guiStateLabel(self.frame, '3:', 4, 0, 'e', varFont, labFont)
		self.lap4 = guiStateLabel(self.frame, '4:', 5, 0, 'e', varFont, labFont)
		self.lap5 = guiStateLabel(self.frame, '5:', 6, 0, 'e', varFont, labFont)
		self.lap6 = guiStateLabel(self.frame, '6:', 7, 0, 'e', varFont, labFont)
		self.lap7 = guiStateLabel(self.frame, '7:', 8, 0, 'e', varFont, labFont)
		self.lap8 = guiStateLabel(self.frame, '8:', 9, 0, 'e', varFont, labFont)
		self.lap9 = guiStateLabel(self.frame, '9:', 10, 0, 'e', varFont, labFont)
		self.lap10 = guiStateLabel(self.frame, '10:', 11, 0, 'e', varFont, labFont)

	def updateList(self, index, lap_time, lap_times):
		if index == 0:
			self.lap0.setVar(lap_time[index])
		elif index == 1:
			self.lap1.setVar(lap_time[index])
		elif index == 2:
			self.lap1.setBgColor(self.validLapTIme(lap_times[index-1]))
			self.lap1.setFgColor('white')
			self.lap2.setVar(lap_time[index])
		elif index == 3:
			self.lap2.setBgColor(self.validLapTIme(lap_times[index-1]))
			self.lap2.setFgColor('white')
			self.lap3.setVar(lap_time[index])
		elif index == 4:
			self.lap3.setBgColor(self.validLapTIme(lap_times[index-1]))
			self.lap3.setFgColor('white')
			self.lap4.setVar(lap_time[index])
		elif index == 5:
			self.lap4.setBgColor(self.validLapTIme(lap_times[index-1]))
			self.lap4.setFgColor('white')
			self.lap5.setVar(lap_time[index])
		elif index == 6:
			self.lap5.setBgColor(self.validLapTIme(lap_times[index-1]))
			self.lap5.setFgColor('white')
			self.lap6.setVar(lap_time[index])
		elif index == 7:
			self.lap6.setBgColor(self.validLapTIme(lap_times[index-1]))
			self.lap6.setFgColor('white')
			self.lap7.setVar(lap_time[index])
		elif index == 8:
			self.lap7.setBgColor(self.validLapTIme(lap_times[index-1]))
			self.lap7.setFgColor('white')
			self.lap8.setVar(lap_time[index])
		elif index == 9:
			self.lap8.setBgColor(self.validLapTIme(lap_times[index-1]))
			self.lap8.setFgColor('white')
			self.lap9.setVar(lap_time[index])
		elif index == 10:
			self.lap9.setBgColor(self.validLapTIme(lap_times[index-1]))
			self.lap9.setFgColor('white')
			self.lap10.setVar(lap_time[index])
		elif index == 11:
			self.lap10.setBgColor(self.validLapTIme(lap_times[index-1]))
			self.lap10.setFgColor('white')
			pass

	def validLapTIme(self, lap_time):
		if lap_time >= TARGET_LAP_TIME_s:
			return '#FF0000'
		elif lap_time < TARGET_LAP_TIME_s:
			return '#5CCB76'


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

		self.lapHandler = lapTimer()

		self.root = tk.Tk()
		self.root.geometry('800x480')
		#self.root.wm_attributes('-fullscreen','true')
		self.root.config(bg='#222F63')

		self.timeFrame = tk.Frame(self.root)
		self.timeFrame.config(bg='white',padx=5,pady=5)
		self.timeFrame.pack(side='right')

		self.mainFrame = tk.Frame(self.root)
		self.mainFrame.config(bg='white')
		self.mainFrame.pack(side='top',padx=5,pady=5)

		self.infoFrame = tk.Frame(self.root)
		self.infoFrame.config(bg='#222F63')
		self.infoFrame.pack(side='top',padx=5,pady=5,fill='y')

		self.errorFrame = tk.Frame(self.root)
		self.errorFrame.config(bg='white')
		self.errorFrame.pack(side='top',padx=5,pady=5)	

		self.Time = guiTimer(self.mainFrame, 1, 0, 'n', self.smallFontBold, self.smallFont)
		self.LapTimes = guiLapTimes(self.timeFrame, 1, 0, 'w', self.smallFontBold, self.smallFont)
		self.Motor1 = guiMotor(self.infoFrame, 1, 1, 0, 'w', self.smallFontBold, self.smallFont)
		self.Motor2 = guiMotor(self.infoFrame, 2, 1, 1, 'w', self.smallFontBold, self.smallFont)
		self.Battery = guiBattery(self.infoFrame, 1, 2, 'w', self.smallFontBold, self.smallFont)

		self.ErrorVar = guiStateLabel(self.errorFrame, 'Battery:', 0, 0, 'e', self.smallFont, self.smallFontBold)
		self.Logging = guiStateLabel(self.errorFrame, 'Logging:', 1, 0, 'e', self.smallFont, self.smallFontBold)
		self.Logging.variablelabel.config(width=7)

	def refresh(self):
		self.root.update_idletasks() 
		self.root.update()

	def updateVals(self, Car):

		self.Time.setTime(self.lapHandler.totalTime())
		self.Time.setAvgLapTime(self.lapHandler.formatSeconds(self.lapHandler.avgLapTime()))
		self.Time.setLapTime(self.lapHandler.currentLapTime())
		self.LapTimes.updateList(self.lapHandler.lap_index, self.lapHandler.formated_lap_times, self.lapHandler.lap_times)
		self.Time.avgLapTime.setFgColor('white')
		self.Time.avgLapTime.setBgColor(self.lapHandler.validLapTIme(self.lapHandler.avgLapTime()))

		self.Motor1.setThrottle(Car.Motor1.Throttle)
		self.Motor1.setCurrent(Car.Motor1.Current)
		self.Motor1.setRPM(Car.Motor1.RPM)
		self.Motor1.setState(Car.Motor1.State)

		self.Motor2.setThrottle(Car.Motor2.Throttle)
		self.Motor2.setCurrent(Car.Motor2.Current/1000)
		self.Motor2.setRPM(Car.Motor2.RPM)
		self.Motor2.setState(Car.Motor2.State)

		self.Battery.setState(Car.Battery.State)
		self.Battery.setCurrent(Car.Battery.Current/1000)

		if (Car.Battery.State == 'Battery Active') | (Car.Battery.State == 'PreCharge'):
			voltage = Car.Battery.Voltage
		else:
			voltage = Car.Battery.Stack_Voltage/10

		self.Battery.setVoltage(voltage/1000)

		errorString = createBatteryErrorString(Car)
		length = len(errorString)
		self.ErrorVar.variablelabel.config(width=length)
		self.ErrorVar.setVar(errorString)	

		if Car.Battery.log.LOGGING:
			self.Logging.setVar('Enabled')
			self.Logging.setBgColor('#37D43D')
		else:
			self.Logging.setVar('Disabled')
			self.Logging.setBgColor('white')