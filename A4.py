import matplotlib.pyplot as plt
import numpy as np
def gradient_descent(f, learning_rate, initial_point):
    def deriv(f, base_point): #estimate the derivative of the function f at base_point using the symmetric approx
        return (f(base_point+10**(-10))-f(base_point-10**(-10)))/(2*10**(-10))

    x_coords=[initial_point] #list to store the x_n's
    y_coords=[f(initial_point)] #list to store the y_n's


    count = 0 #safety counter, used to stop loop if it goes too far
    while abs(deriv(f, x_coords[-1]))>10**(-5): #while the derivative is not close to 0
        x_coords.append(x_coords[-1]-learning_rate*(deriv(f, x_coords[-1]))) #update list of x_n based on f(x0)-learning_rate*f'(x0)
        y_coords.append(f(x_coords[-1])) #update y_n
        if count > 100000: #if more than 10000 steps are taken, break out of the loop and end the program
            break             
        count += 1

    plot_range=np.linspace(min(x_coords)-0.5, max(x_coords)+0.5,10000) 
    function_range=[f(i) for i in plot_range]
    plt.plot(plot_range, function_range) 
    plt.plot(x_coords, y_coords) 
    plt.show()
    return print('('+str(round(x_coords[-1],3))+ ','+ str(round(y_coords[-1],3))+')'),print(count)#this will print the minima as a (x,y) pair

def quadratic(x): #defined quadratic 
    return x**2

def polynomial(x): #defined polynomial
    return (x**4)-(2*(x**2))

def funny_function(x): #defined funny function
    if x>0:
        return x**x
    elif x==0:
        return 1
    else:
        return abs(x)**abs(x)
    
#Finding minima of quadratic
gradient_descent(quadratic, 0.1, 5)

#Finding both minima of a polynomial
gradient_descent(polynomial, 0.001, 2)
gradient_descent(polynomial, 0.001, -2)

#Finding both minima of funny_function
gradient_descent(funny_function, 1e-1, 1)
gradient_descent(funny_function, 1e-1, -1)

#Finding minima of absolute value
gradient_descent(abs,1e-4,1)

