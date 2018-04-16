from math import *
import numpy as np 
#import math as m

def main():
  #print("Hello World!")
  L = []
  h = []
  h = [1,1]
  #h.append(1)
  #h.append(1)
  #print(sigma(h,h))
  #print(L_simple(h))
  #print(L_simple_dw1(h))
  #print(L_simple_dw2(h))
  #eta = 0.00001
  #for j in range(1,8):
 # 	eta = eta*10
  eta = 10
  iter = 1000
  print(minimize_loss([0,0],eta, iter))
  #w = []
  #w_min = []
  #for i in range(-6,6):
  #	for j in range(-6,6):
  #		w=[i,j]
  #		w_min.append(minimize_loss(w, 1, 100))

  #return min(w_min)



def minimize_loss(w, eta,iter):
	#want to test all possible values of w[-6,-6]; update w_i
	# and minimize L_simple
	w_1old =w[0]
	w_2old =w[1] 
	value_arr = []
	for i in range(1,iter):
		w_1new = w_1old - eta*L_simple_dw1([w_1old,w_2old])
		w_2new = w_2old - eta*L_simple_dw2([w_1old,w_2old])
		print(w_1new, w_2new)
		w_1old = w_1new
		w_2old = w_2new 
		L_simpleval= L_simple([w_1new,w_2new])
		value_arr.append(L_simpleval)
		if min(value_arr) == L_simpleval:
			w_minimize = [w_1new, w_2new]
	return w_minimize

def sigma(w,x): 
	#assumes user inputs 1X2 array 
	func_val = 1/(1+exp(-(w[0]*x[0] + w[1]*x[1])))
	return func_val

def L_simple(w):
	func_val = pow((sigma(w,[1,0])-1),2) \
			 + pow((sigma(w,[0,1])),2) \
			 + pow((sigma(w,[1,1])-1),2)
	return func_val

def L_simple_dw1(w):
	func_val = (-2)/pow((1+exp(-w[0])),3)-2/pow((1+exp(-w[0] - w[1])),3)
	return func_val

def L_simple_dw2(w): 
	func_val = (-2)/pow((1+exp(-w[1])),3)-2/pow((1+exp(-w[0] - w[1])),3)
	return func_val
	



















if __name__== "__main__":
  main()

