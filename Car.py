
class Motor_c:
	def __init__(self):
			self.Running = False
			self.Current_Limit = False
			self.Voltage_Limit = False
			self.RPM = 0
			self.Current = 0
			self.PWM = 0
			self.Throttle = 0


class Battery_c:
	def __init__(self): 
			self.States = 0
			self.Current = 0
			self.Voltage = 0
			self.Cell_Voltage = [12]
			self.Cell_Temp = [4]


class Car_c:
	def __init__(self):
			self.Lights = False
			self.Window_Wiper = False
			self.Emergency_Stop = False
			self.Emergency_Lights = False
			self.Deadmanswitch = False
			self.Cruise_Control = False
			self.CC_Velocity = 0
			self.Throttle = 0
			self.Velocity = 0
			self.RPM = 0
			self.Torque = 0
			self.Acceleration = 0
			self.Brake = False
			self.Motor1 = Motor_c()
			self.Motor2 = Motor_c()
			self.Battery = Battery_c()

 
