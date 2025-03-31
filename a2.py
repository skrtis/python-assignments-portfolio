import numpy as np
np.seterr(divide = 'ignore') 

def roots(f,a,b):
    c = a 
    d = b
    while abs(d - c) > (2*10**(-10)): # double the required accuracy, as it is approaching from two sides
        mid = (c+d)/2 # make the midpoint
        #edge cases
        if f(c) == 0: 
            return c
        elif f(d) == 0: 
            return d
        elif f(mid) == 0:
            return mid 

        # First check corollary (Bolzano's Theorem)
        if f(c)<=0<=f(d) or f(d)<=0<=f(c):
            if f(c)<=0<=f(mid) or f(mid)<=0<=f(c): 
                d = mid 
            elif f(mid)<=0<=f(d) or f(d)<=0<=f(mid):
                c = mid 
            else:
                return "root not in range"
        else:
            return "Not obtainable by bisection."

    return round((c+d)/2,10)

# test functions
def f1(x):
    y = np.exp(x)+ np.log(x)
    return y

def f2(x):
    y = np.arctan(x) - (x**2)
    return y

def f3(x): 
    y = np.sin(x)/np.log(x)
    return y

def f4(x):
    y = np.log(np.cos(x))
    return y


print(roots(f1,0,1))
print(roots(f2,0,2))
print(roots(f3,3,4))
print(roots(f4,5,7))
