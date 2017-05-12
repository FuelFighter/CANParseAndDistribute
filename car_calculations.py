TIRE_DIAMETER = 0.55
RPM_TO_METER_P_SECOND = TIRE_DIAMETER * 3.14159 / 60

def calculateVelocity(RPM):
	return RPM*RPM_TO_METER_P_SECOND

def calculateKmh(velocity):
	return velocity*3.6