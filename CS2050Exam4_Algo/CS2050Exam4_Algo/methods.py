import math
primeFac = [1, ]

def primeFactors(n):
    temp=n
    try:
        if n <=0:
            raise ArithmeticError("Number has to be greater than 0")
        else:
   
    # Print the number of two's that divide n 
            while n % 2 == 0: 
                primeFac.append(2)
                n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
            for i in range(3,int(math.sqrt(n))+1,2): 
        # while i divides n , print i ad divide n 
                while n % i== 0: 
                    primeFac.append(i)
                    n = n // i 
              
    # Condition if n is a prime 
    # number greater than 2 
            if n > 2: 
                primeFac.append(n)
                primeFac.append(temp)
            return primeFac
    except ArithmeticError as err:
        return err.args
# Driver Program to test above function 

def findMod(num, modBy, expo):
    x=num
    for i in range(1,expo):
        num = (x*num) % modBy
    return num

def sumArithmetric(initialTerm,difference,num):
   try:
        if num<1:
            raise ArithmeticError("N has to greater than or equal to 1")
        else:
            return (int)(initialTerm*num + (num*difference*(num-1)//2))
   except ArithmeticError as err:
        return(err.args)
   

def sumGeometric(initialTerm,commonRatio,n):
    try:
        if n<1:
            raise ArithmeticError("N has to greater than or equal to 1")
        elif commonRatio==1:
            raise ArithmeticError("Common Ratio Cannot be 1")
        else:
               return (int)(initialTerm*(math.pow(commonRatio,n) -1)//(commonRatio-1))
    except ArithmeticError as err:
        return(err.args)
 
def addMod(num1, num2, modBy):
    return ((num1+num2)% modBy)

def multiplyMod(num1,num2,modBy):
    return ((num1)*(num2) % modBy)

# Recursive function to return gcd of a and b 
def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
  
# Function to return LCM of two numbers 
def lcm(a,b): 
    return (a*b) / gcd(a,b) 
  
def isPrime(num):
    y = math.floor(math.sqrt(num))
    for i in range(2,y+1):
        if num % i == 0:
            return ("Composite")
    return("Prime")

def primeFacTheorem(num):
    return (1/math.log(num))

def inverseMod(num, modBy):
    for i in range(1,modBy):
        if(i*num % modBy == 1):
            return i


def swap(x,y):
    temp = x
    x =y 
    y = temp
    return(x,y)

#Euclids algo tp find the GCM 
#Input: Two positive integers, x and y.
#Output: gcd(x, y).
#def euclid_GCM(x, y):
#    if(y<x):
#       x,y = swap(x, y)
#    r = y % x

#    while(r!= 0):
#        y = x
#        x = r
#        r = y % x
#    return r

#Algorithm to find the base b expansion for a positive integer.
#Input: Integers n and b. b > 1 and n ≥ 1.
#Output: Base b expansion of n. Base b digits are output in reverse order.
def bExpansion(num, base):
    x = num
    count = 0
    y =0 
    while(x > 0):
        y += (x % base) * math.pow(10,count)
        x = x // base
        count +=1

    return y

def factorial(n):
    if(n==0):
        return 1
    elif(n==1):
        return 1
    return n*factorial(n-1)

def permutation(n, r):
    #if(n-r + 1 == 0):
    #    return 1
    #return(n*permutation(n-1,r))
    if(r>n):
        n,r = swap(n,r)
    n,r = factorial(n), factorial(n-r)
    return n//r

def combination(n,r):
     if(r>n):
        n,r = swap(n,r)
     n,r,nr = factorial(n),factorial(r), factorial(n-r)
     return n//(r*nr)

def fast_modular_expo(num1,num2, modBy):
    partialResult = 1
    current = num1
    binaryExpansion = y

    while(binaryExpansion>0):
        if(binaryExpansion%2 ==1):
            partialResult = partialResult*current % modBy
        current = current*current % modBy
        binaryExpansion = binaryExpansion // 2

    return partialResult

#def genLexPermutations(n):
#    p=[]
#    for i in range(1,n+1):
#        p.append(i)
#    print(p)
#    while p != p.reverse():
#        p = nextPerm(p)
#        print(p)
#def nextPerm(*arg):
#    k = arg.count()
