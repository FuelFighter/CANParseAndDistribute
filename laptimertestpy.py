import time as time
import random as random


class lapTimer():
	startup_time = 0
	lap_times = [0.0]
	lap_timestamps = [0.0]
	formated_lap_times = ['']
	lap_index = 0

	def __init__(self):
		self.startup_time = time.time()

	def updateTimer(self):
		self.current_time = time.time()
		if self.lap_index == 0:
			self.lap_times[self.lap_index] = self.current_time - self.startup_time
		else: 
			self.lap_times[self.lap_index] = self.current_time - self.lap_timestamps[self.lap_index-1]

		self.lap_timestamps[self.lap_index] = self.current_time
		self.formated_lap_times[self.lap_index] = self.formatSeconds(self.lap_times[self.lap_index])

	def formatSeconds(self, seconds):
		seconds = int(seconds*1000)
		s, ms = divmod(seconds,1000)
		m, s = divmod(s, 60)
		time_string = ('%02dm:%02ds:%02dms') % (m, s, ms)
		return time_string

	def newLap(self):
		self.updateTimer()
		self.lap_times.append(0.0)
		self.lap_timestamps.append(0.0)
		self.formated_lap_times.append('')
		self.lap_index = self.lap_index + 1 

	def returnCurrentLapTime(self):
		return self.formatSeconds(self.lap_times[self.lap_index])






def main():
	laptimer = lapTimes()

	count = 0
	numLaps = 0

	ceiling = int(random.random()*1500)
	print('Target: '+ str(ceiling))

	while(1):

		if count >= ceiling:
			print(laptimer.returnCurrentLapTime())
			laptimer.newLap()
			ceiling = int(random.random()*1500)
			print('New Target: ' + str(ceiling))
			numLaps = numLaps + 1
			count = 0

		if numLaps == 5:
			break

		count = count + 1
		time.sleep(0.01)
		laptimer.updateTimer()

	for lap_time in laptimer.formated_lap_times:
		print(lap_time)


if __name__ == '__main__':
	main()