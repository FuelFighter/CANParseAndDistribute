import random as random
import math as math


Array = [0]*10

for x in range(0,10):
	Array[x] = random.random()*10

print(Array)

value = 0.0
for y in Array[1:5]:
	value = value + y

print(value)
value = math.ceil(value)
print(value)


value = 0.0
for z in Array[1:5]:
	value = value + math.ceil(z)
print(value)