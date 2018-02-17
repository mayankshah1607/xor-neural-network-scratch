#A NEURAL NETWORK THAT LEARNS XOR LOGIC

import numpy as np  

x1 = np.array([0,1,0,1])  #Training Input
x2 = np.array([0,0,1,1])

and_op = np.array([0,0,0,1]) #Training Output
or_op = np.array([0,1,1,1])

learning_rate = 0.01	#Learning Rate

def sig(z):				#Sigmoid Function
    return 1 / (1 + np.exp(-(z)))

#Learn AND/OR using Gradient Descent
def learn(x1,x2,y): 
	#Parameters initially assigned to Zero
	t1 = 0	
	t2 = 0
	t3 = 0
	#Perform 10000 iteration
	for i in range(10000): 
		gradient1 = 0
		gradient2 = 0
		gradient3 = 0
		#Calculate derivative
		for j in range(len(x1)):	
			gradient1 = gradient1 + (sig(t1+(t2*x1[j])+t3*x2[j]) - y[j])
			gradient2 = gradient2 + (sig(t1+(t2*x1[j])+t3*x2[j]) - y[j]) * x1[j] 
			gradient3 = gradient3 + (sig(t1+(t2*x1[j])+t3*x2[j]) - y[j]) * x2[j]
		#Update weights
		t1 = t1 - ((learning_rate/len(x1)) * gradient1) 	 
		t2 = t2 - ((learning_rate/len(x1)) * gradient2)
		t3 = t3 - ((learning_rate/len(x1)) * gradient3)
	return (t1,t2,t3) #Return weights

def learn_not(x,y): #Learning AND / OR
	#Parameters initalized to zero
	t1 = 0
	t2 = 0
	#Iterate 10000 times
	for i in range(10000):
		gradient1 = 0
		gradient2 = 0
		gradient3 = 0
		#Calculate gradient
		for j in range(len(x)):
			gradient1 = gradient1 + (sig(t1+(t2*x1[j])) - y[j])
			gradient2 = gradient2 + (sig(t1+(t2*x1[j])) - y[j]) * x[j] 
		#Update weights
		t1 = t1 - ((learning_rate/len(x1)) * gradient1)
		t2 = t2 - ((learning_rate/len(x1)) * gradient2)
	return (t1,t2) #Return weights

#Weight matrix
and_params = learn(x1,x2,and_op)
or_params = learn(x1,x2,or_op)
not_params = learn_not([0,1],[1,0])

#Get new Input
ip1 = int(input('Enter value 1 :'))
ip2 = int(input('Enter value 2 :'))


#CONSTRUCTION OF NEURAL NETWORK

#[a,b] vector forms input layer
#layer1 [0] = A'.B
#layer1 [1] = A.B'
#Output layer = A'.B + A.B'

#Calculate NOT using input and weight matrix
def getNot(x):
	ans = sig(not_params[0] + x*not_params[1])
	if (ans>0.5) : return 1
	else : return 0

#Calculate AND/OR using inputs and weight matrix 
def getVal(x1,x2,func):
	if (func=='and'):
		ans = sig(and_params[0] + x1*and_params[1] + x2*and_params[2])
		if (ans>0.5) : return 1
		else : return 0
	elif (func=='or') :
		ans = sig(or_params[0] + x1*or_params[1] + x2*or_params[2])
		if (ans>0.5) : return 1
		else : return 0
	else :
		print(func,' not a defined attribute')

#Getting activated values at Layer1
a1 = getVal(getNot(ip1),ip2,func = 'and') 
a2 = getVal(ip1,getNot(ip2),func='and')

#Forming hidden layer
layer1 = [a1,a2] 

#calculating Output
output = getVal(a1,a2,func='or')

print('XOR OUTPUT IS : ',output)