

# Author: vlarobbyk

import matplotlib.pyplot as pp
import numpy as np
import random

class RandomValuesGenerator:
	
	def __init__(self, total_points=1000):
		self.total_points=total_points
		
	
	def fx(self,x):
		y=0.01*np.power(x,3.)+0.01*np.power(x,2.)-0.001*x
		return y
	
	
	def plot_data(self):
		x=np.arange(1.,13.,0.23)
		y=self.fx(x)
		
		rv=np.random.uniform(0.,1.,size=len(x))
		mul=np.random.uniform(1.,4.7,size=len(x))
		choices=[random.choice((-1.,1.)) for i in range(len(x))]
		colors=['blue' if k==1 else 'red' for k in choices]
		prod=np.multiply(rv,np.multiply(mul,choices))
		
		
		print(prod)
		
		pp.scatter(x,np.add(prod,y),color=colors)
		pp.show()
		
if __name__=="__main__":
	randomg=RandomValuesGenerator()
	x=np.arange(1.,13.,0.103)
	randomg.plot_data()
