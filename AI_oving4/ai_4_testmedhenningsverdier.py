#from mpl_toolkits.mplot3d import Axes3D
#import matplotlib.pyplot as plt
from math import *
import numpy as np 



def main():
  
  
  eta = 0.00001
  iter = 10000
  #for j in range(1,8):
 	#eta = eta*10
  	#print(minimize_loss([-6,-6],eta, iter), eta, [ -6, -6]) #Task 1_2   	
  print(minimize_loss([-6,-6],eta, iter), eta) #Task 1_2   	
  return



def minimize_loss(w, eta,iter):
	#want to test all possible values of w[-6,-6]; update w_i
	# and minimize L_simple
	
	w_old = w
	value_arr = []
	for i in range(1,iter):
		w_new = w_old - np.array([eta, eta])*d_L_simple([w_old[0], w_old[1]])
		w_old = w_new
		L_simpleval= L_simple([w_new[0],w_new[1]])
		value_arr.append(L_simpleval)
		if min(value_arr) == L_simpleval:
			w_minimize = [w_new[0], w_new[1]]
	plotL_simple(eta, value_arr)
	return w_minimize

def logistic(w,x): 
    return 1.0/(1.0+np.exp(-np.inner(w,x)))

def d_logistic(w,x,derivative):
    if derivative == 1:
        return x[0] * np.exp(-np.inner(w,x))*logistic(w, x)*logistic(w, x)
    if derivative == 2:
        return x[1] * np.exp(-np.inner(w,x))*logistic(w, x)*logistic(w, x)

def L_simple(w):
    return np.power(logistic(w, [1, 0]) -1, 2) + np.power(logistic(w, [0, 1]), 2) + np.power(logistic(w, [1, 1]) -1, 2)

def d_L_simple(w):
    #derivate of L_simple    
    first_w1 = (logistic(w, [1, 0]) -1) * 2 * d_logistic(w, [1, 0], 1) 
    second_w1 = (logistic(w, [0, 1])) * 2 * d_logistic(w, [0, 1], 1) 
    third_w1 = (logistic(w, [1, 1]) -1) * 2 * d_logistic(w, [1, 1], 1) 

    first_w2 = (logistic(w, [1, 0]) -1) * 2 * d_logistic(w, [1, 0], 2) 
    second_w2 = (logistic(w, [0, 1])) * 2 * d_logistic(w, [0, 1], 2) 
    third_w2 = (logistic(w, [1, 1]) -1) * 2 * d_logistic(w, [1, 1], 2) 
    return [first_w1 + second_w1 + third_w1, first_w2 + second_w2 + third_w2]

def plotL_simple(eta, val_arr):
	fig = plt.figure() 
	ax = fig.gca(projection='3d')

	# Plot a sin curve using the x and y axes.
	x = np.linspace(0, 1, 100)
	y = np.sin(x * 2 * np.pi) / 2 + 0.5
	ax.plot(x, y, zs=0, zdir='z', label='curve in (x,y)')
	return








if __name__== "__main__":
  main()

