import math 
from methods import *

method = ["""
1. Find prime Factors, 
2. Find the Sum of Arithmetic sequence, 
3. Find the sum of Geometric Sequence, 
4. Find the GCD, 
5. Find the LCM, 
6. Find whether the num is prime or not,
7. Find base b expansion, 
8. Factorial, 
9. Permutation, 
10. Combination,
11. Fast modular Expo
"""]

def main():
    print("Discrete Math Calculator")
    for i in method:
        print(i)

    choice = input("Enter Choice: ")
    
    if(choice=="1" or choice[0:5] == "prime"):
        num=int(input("Enter the number you want the prime factors of: "))
        print(primeFactors(num))

    elif(choice=="2" or choice[0:3]=="ari"):
        initialTerm = int(input("Enter the initial Term: "))
        difference= int(input("Enter the difference: ")) 
        numTerms = int(input("Enter total number of terms: "))
        print(sumArithmetric(initialTerm, difference, numTerms))

    elif(choice=="3" or choice[0:3]=="geo"):
        initialTerm = int(input("Enter the initial Term: "))
        difference= int(input("Enter the difference: ")) 
        numTerms = int(input("Enter total number of terms: "))
        print(sumGeometric(initialTerm, difference, numTerms))

    elif(choice=="4" or choice[0:3].lower=="gcd"):
        num, div = int(input("Enter two numbers you want gcd of: "))
        print(gcd(num,div))

    elif(choice=="5" or choice[0:3].lower=="lcm"):
        num, div = int(input("Enter two numbers you want lcm of: "))
        print(lcm(num,div))

    elif(choice=="6"):
        num = int(input("Check whether a number is prime or not: "))
        print(isPrime(num))

    elif(choice=="7" or choice[0:13].lower =="base expansion"):
        num = int(input("Enter the number: "))
        base = int(input("Base: "))
        print(bExpansion(num,base))

    elif(choice=="8" or choice[0:8].lower=="factorial"):
        num= int(input("Enter the number "))
        print(factorial(num))

    elif(choice=="9" or choice[0:11].lower=="permutation"):
        num = int(input("Enter n: "))
        b = int(input("Enter r: "))
        print(permutation(num,b))

    elif(choice=="10" or choice[0:12].lower=="combination"):
        num = int(input("Enter n: "))
        r = int(input("Enter r: "))
        print(combination(num,r))

    elif(choice=="11" ):
        num1 = int(input("Enter the number "))
        num2 = int(input("Enter num 2: "))
        modBy = int(input("Enter the number you want to mod by: "))
        print(fast_modular_expo(num1,num2,modBy))

    elif(choice=="q"):
        print("Thank you!")
        exit(0)
    else: 
        print("Invalid Choice")
    choice=input("Enter a Choice: ")

if __name__ == "__main__":
    main()