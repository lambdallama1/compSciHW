#!/usr/bin/python3

import matplotlib.pyplot as plt
import scipy.interpolate as inter
import numpy as np

x = list(range(-4, 5))
y =[1.125e-07, 1.234e-04, 1.832e-02, 3.679e-01, 1, 3.679e-01, 1.832e-02, 1.234e-04, 1.125e-07]
inter_f = np.poly1d(np.polyfit(x, y, 9)) 
inter_x = np.arange(-4, 4, 0.1)
inter_y = inter_f(inter_x)
plt.plot(x, y,'o', inter_x, inter_y, '-')
plt.title("9th Order Polynomial Interpolation of Data Points")
plt.legend(["Data", "9th Order Polynomial"])
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("1(i).png")


cubic_spline = inter.make_interp_spline(x, y, k=3) 
lin_spline = inter.make_interp_spline(x, y, k=1) 
inter_x = np.arange(-4, 4, 0.1)
plt.figure()
plt.plot(x, y,'o', inter_x, lin_spline(inter_x), '-', inter_x, cubic_spline(inter_x))
plt.legend(["Data", "Linear Spline", "Cubic Spline"])
plt.title("Linear and Cubic Spline of Data")
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("1(ii).png")

