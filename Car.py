import time as t

class Motor_c:
	def __init__(self):
			self.State = ""
			self.Current_Limit = False
			self.Voltage_Limit = False
			self.RPM = 0
			self.Current = 0
			self.PWM = 0
			self.Throttle = 0
			self.Temp = 0


class Battery_c:
	def __init__(self): 
			self.State = ""
			self.Error_PreChargeTimeout = False
			self.Error_LTC_LossOfSignal = False
			self.Error_OverVoltage = False
			self.Error_UnderVoltage = False
			self.Error_OverCurrent = False
			self.Error_OverTemp = False
			self.Error_NoDataOnStartup = False
			self.Current = 0
			self.Voltage = 0
			self.Cell_Voltage = [0,0,0,0,0,0,0,0,0,0,0,0]
			self.Cell_Temp = [0,0,0,0]


class Car_c:
	def __init__(self):
			self.Lights = False
			self.LapButton = False
			self.Window_Wiper = False
			self.BlinkerLeft = False
			self.BlinkerRight = False
			self.Emergency_Stop = False
			self.Emergency_Lights = False
			self.Deadmanswitch = False
			self.Cruise_Control = False
			self.CC_Velocity = 0
			self.Throttle = 0
			self.Velocity = 0
			self.AvgVel = 0
			self.RPM = 0
			self.Torque = 0
			self.Acceleration = 0
			self.Brake = False
			self.Motor1 = Motor_c()
			self.Motor2 = Motor_c()
			self.Battery = Battery_c()
			self.FirstTime = t.time()
			self.LapTimes = []
			self.LapTimeIndex = 0 

 
