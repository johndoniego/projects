#Example 1:

# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.interpolate import interp1d

# x=np.array([0, 1, 2, 5])
# y=np.array([2, 3, 12, 147])
# plt.plot(x,y, color='red', linewidth = 3, marker='o',markerfacecolor='green', markersize=12)

# f=interp1d(x,y,kind='cubic')
# xnew=np.linspace(x[0],x[-1])

# plt.plot(xnew,f(xnew), color='black', marker='*')
# plt.show()


#Example 2:

# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.interpolate import interp1d

# x=np.linspace(0,10,num=11)
# y=np.cos(-x**2/9.0)

# f=interp1d(x,y)
# f2=interp1d(x,y,kind='cubic')
# xnew=np.linspace(0,10,num=41)

# plt.plot(x,y,'o',xnew,f(xnew), '-',xnew,f2(xnew),'--')
# plt.show()


#Example 3:

# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.interpolate import interp1d

# x=np.linspace(0,10,num=11)
# y=np.cos(-x**2/9.0)

# f1=interp1d(x,y,kind='nearest')
# f2=interp1d(x,y,kind='previous')
# f3=interp1d(x,y,kind='next')
# xnew=np.linspace(0,10,num=41)

# plt.plot(x,y,'o',xnew,f1(xnew),'-',xnew,f2(xnew),'--',xnew,f3(xnew),':')
# plt.legend(['data','nearest','previous','next'])
# plt.show()


