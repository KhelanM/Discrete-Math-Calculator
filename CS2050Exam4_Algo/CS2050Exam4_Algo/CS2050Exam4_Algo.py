import math 
from methods import *
#import methods

method = ["""
1. Find prime Factors, 
2. Find the Sum of Arithmetic sequence, 
3. Find the sum of Geometric Sequence, 
4. Find the GCD, 
5. Find the LCM, 
6. Find whether the num is prime or not,
7. Find prime Factors, 
8. Find base b expansion, 
9. Factorial, 
10. Permutation, 
11. Combination,
12. Fast modular Expo
"""]

print("Discrete Math Calculator")
for i in method:
    print(i)

choice = input("Enter Choice: ")

if(choice=="1" or choice[0:5] == "prime"):
    num=int(input("Enter the number you want the prime factors of: "))
    print(primeFactors(num))


elif(choice=="2" or choice[0:3]=="mod"):
    initialTerm, difference, commonRatio = input("Enter the initial Term, difference, and number of terms: ")
    print(sumArithmetric(int(initialTerm, difference, commonRatio)))

elif(choice=="3" or choice[0:3]=="mod"):
    num, div = input("Enter the number ")
    print()

elif(choice=="4" or choice[0:3]=="mod"):
    num, div = input("Enter the number ")
    print()

elif(choice=="5" or choice[0:3]=="mod"):
    num, div = input("Enter the number ")
    print()

elif(choice=="6" or choice[0:3]=="mod"):
    num, div = input("Enter the number ")
    print()

elif(choice=="7" or choice[0:3]=="mod"):
    num, div = input("Enter the number ")
    print()