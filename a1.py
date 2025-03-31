x = float(input("input:")) #takes input
def fullapprox(x):#defines the entire function 
    if x >= 0 and x <=1: #checks if x is valid
        def approx(x,n): #define approximation function
            i = 0 
            z = 0
            while i <= n:
                y = (((-1)**i)*(x**((2*i)+1)))/((2*i)+1)
                z += y
                i += 1
            return z 

        def error(x,n): #defines error function
            b = (x**(2*n+1))/(2*n+1) 
            return b
        
        #initialize n
        n = 0 
        #while loop finds n for error being <=0.0001
        while error(x,n) >= 0.0001: 
            n += 1  
    else:
        return("Error: x not within [0,1]")
    return approx(x,n),n,error(x,n)

print(fullapprox(x))
