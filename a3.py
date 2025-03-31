import time
import numpy as np
start_time = time.time()

def quadratic(x):
    return x**2

def sin(x):
    return np.sin(x)

def exponential(x):
    return np.exp(x)


def linear_approximation(f,c,E):
    # central difference derivative
    dx = 1e-8
    d = (f(c+dx)-f(c-dx))/(2*dx)

    x1 = c
    x2 = c

    error1 = abs(f(x1)-f(c)-(d*(x1-c)))
    error2 = abs(f(x2)-f(c)-(d*(x2-c)))

    while error1<E:
        error1 = abs(f(x1)-f(c)-(d*(x1-c)))
        x1-=1e-5

        if time.time()-start_time>30:
            return "Runtime > 30 seconds."
    
    while error2<E: 
        error2 = abs(f(x2)-f(c)-(d*(x2-c)))
        x2+=1e-5

        if time.time()-start_time>30:
            return "Runtime > 30 seconds."

    return float(x1),float(x2)


print(linear_approximation(quadratic,1,0.1))
print(linear_approximation(sin,np.pi/4,0.05))
print(linear_approximation(exponential,0,0.01))
print("--- %s seconds ---" % (time.time() - start_time)) 