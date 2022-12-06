import json
import numpy
import random

def demo():
	otp = random.randint(0,9)
	print(otp)
	v = otp%2
	if v == 0:
		raise ValueError('value error')
	else:
		return "completed"

demo()
