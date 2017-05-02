import string

CANID = {
	'Brake':0x110,
	'Encoder':0x220,
	'Steering Wheel':0x230,
	'Dashboard':0x310,
	'BMS Cell V 1-4':0x440,
	'BMS Cell V 5-7':0x441,
	'BMS Cell V 8-12':0x442,
	'BMS Cell Temp':0x443,
	'BMS Volt Current':0x444,
	'BMS Status':0x448,
	'BMS Error Flags':0x449,
	'Motor 1 Status':0x450,
	'Motor 2 Status':0x460,
	'Front Lights Status':0x470,
	'Back Lights Status':0x480
}


def parseCANString(line):

	line = line.strip('[]')
	lineArray = line.split(':')

	ID = int('0x' + lineArray[0],16)
	Length = int('0x' + lineArray[1],16)
	Data = []

	for pos in range(0,Length):
		Data.append(lineArray[2][(2*pos):(2*pos+2)])

	return ID, Data


