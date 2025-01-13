#Example 1: What is an integral of 2x? where x is equal to 3

# from scipy.integrate import quad #import needed library 
# def f(x):				#function that holds the equation
#     return 2*x
# i,err=quad(f,0,3)			#quad function 
# print(i)


#Example 2: What is an integral of x3?where x is equal to 3

# from scipy.integrate import quad #import needed library 
# def f(x):				#function that holds the equation
#     return x**3
# i,err=quad(f,0,3)			#quad function 
# print(i)


#Example 3: What is an integral of 2x+p?where p is a parameter

# Example 3.A

# from scipy.integrate import quad 	#import needed library
# def f(x):					#function that holds the equation
#     return 2*x+p
# p=4					#global variable for parameter
# i,err=quad(f,0,3)				#quad function
# print(i)

# Example 3.B

# from scipy.integrate import quad
# def f(x,p):				#passing the value of parameter
#     return 2*x+p

# i,err=quad(f,0,3,args=4)		#Using args 
# print (i)