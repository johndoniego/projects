#1.Using Python List

# x=[0, 1, 2, 5]				# x-axis
# y=[2, 3, 12, 147]				# y-axis

# xp=3						# x value
# yp=0						# missing y value

# for i in range(4):			# compute for the P(x)
#     p=1					# initial value of p 
#     for j in range(4):			# compute for Pi (x)
#         if j!=i:
#             p*=(xp-x[j])/(x[i]-x[j])		
#     yp+=y[i]*p				# compute for P(x)

# print( ' x:%f y:%f ' % (xp,yp))


#2.User Input

# x=[0, 1, 2, 5]
# y=[2, 3, 12, 147]

# n=len(x)			# get the number of element on the list
# xp=int(input('Enter x-axis:')) # get x value from the user	
# yp=0
# for i in range(n):
#     p=1
#     for j in range(n):
#         if j!=i:
#             p*=(xp-x[j])/(x[i]-x[j])
#     yp+=y[i]*p

# print('x:%f y:%f' %(xp,yp))


#3.Using Numpy Array

# import numpy as np			# import the needed package

# x=np.array([0, 20, 40, 60, 80, 100])	# set numpy array
# y=np.array([26.0, 48.6, 61.6, 71.2, 74.8, 75.2])

# xp=float(input('Enter x-axis:')) 	# get value from the user
# yp=0

# for xi,yi in zip(x,y):				# loop for xi and yi
#     p=np.prod((xp-x[x!=xi])/(xi-x[x!=xi]))#compute Pi(x)
#     yp+=yi*p					# compute for P(x)

# print('x:%f y:%f' %(xp,yp))


#4.Plotting the Lagrangian Interpolation Using Python List

# import matplotlib.pyplot as plt 	# import the needed package
# x=[0, 1, 2, 5]				# x axis
# y=[2, 3, 12, 147]				# y axis

# n=len(x)					# length of x axis
# xp=float(input('Enter x-axis:'))	# given x value
# yp=0
# for i in range(n):
#     p=1
#     if xp>x[i] and xp<=x[i+1]:	
#         ins=i+1			# identifying the index of x value
#     for j in range(n):
#         if j!=i:
#             p*=(xp-x[j])/(x[i]-x[j])
#     yp+=y[i]*p

# x.insert(ins,xp)			# add xp to x axis
# y.insert(ins,yp)			# add yp to y axis

# plt.plot(x,y, color='green', linewidth = 3, 
#          marker='o', markerfacecolor='red', 
#    markersize=12)		# plot x,y axis
# plt.show()


#5.Plotting the Lagrangian Interpolation Using Numpy Array

# import numpy as np
# import matplotlib.pyplot as plt 

# x=np.array([0, 1, 2, 5])
# y=np.array([2, 3, 12, 147])

# xp=float(input('Enter x-axis:')) 	# get value from the user
# yp=0

# for xi,yi in zip(x,y):
#     if xp>xi and xp<=xi+1:	# identifying the index of x value
#         ins=xi+1
#     p=np.prod((xp-x[x!=xi])/(xi-x[x!=xi]))#compute Pi(x)
#     yp+=yi*p					# compute for P(x)

# x=np.insert(x, ins, xp)		# add xp to x axis
# y=np.insert(y, ins, yp)		# add yp to y axis

# plt.plot(x,y, color='red', linewidth = 3, 
#          marker='o', markerfacecolor='green', 
#    	   markersize=12)
# plt.show()


#6.Plotting the Lagrangian Interpolation Using Numpy linspace() function

# import numpy as np
# import matplotlib.pyplot as plt 

# #first array
# x=np.array([0, 1, 2, 5])
# y=np.array([2, 3, 12, 147])

# #2nd array
# xplt=np.linspace(x[0], x[-1])
# yplt=np.array([])

# #lagrange 
# for xp in xplt:
#     yp=0
#     for xi,yi in zip(x,y):
#         p=np.prod((xp-x[x!=xi])/(xi-x[x!=xi]))
#         yp+=yi*p
#     yplt=np.append(yplt, yp)

# #plot 1st array
# plt.plot(x,y, color='red', linewidth = 3, marker='o',    markerfacecolor='green', markersize=12)

# #plot 2nd array
# plt.plot(xplt,yplt)
# plt.show()
