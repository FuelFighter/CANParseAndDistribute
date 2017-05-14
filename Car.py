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


class Interface_c:
	def __init__(self):
			self.Brake = False
			self.Light_Level = 0
			self.LapButton = False
			self.WindowWiper_State = False
			self.WindowWiper_Speed = 0
			self.HazardLights = False
			self.BlinkerLeft = False
			self.BlinkerRight = False
			self.CC_Button = False
			self.Horn = False
			self.ThrottleLeft = 0
			self.ThrottleRight = 0
			self.Deadmanswitch = False


class Lights_c:
			self.Headlights = False
			self.Headlight_Level = 0
			self.Brakelights = False
			self.RearLights = False
			self.RearLight_Level = 0
			self.BlinkerLeft = False
			self.BlinkerRight = False


class Time_c:
			self.FirstTime = t.time()
			self.TotalTime = 0
			self.LapTimes = []
			self.LapTimeIndex = 0


class Car_c:
	def __init__(self):
			self.CC_Velocity = 0
			self.Throttle = 0
			self.Velocity = 0
			self.AvgVel = 0
			self.RPM = 0
			self.Torque = 0
			self.Acceleration = 0

			self.Motor1 = Motor_c()
			self.Motor2 = Motor_c()
			self.Battery = Battery_c()
			self.Lights = Lights_c()
			self.Interface = Interface_c()

 
