#Recursive
import time

n=int(input("Enter number for print: "))

start_time=time.time()
print("Start time: ",start_time)
a=0
b=1
sum=0

print("Fibonacci Series is: ")

def fibo(i):
    if(i<=1):
        return i
    else:
        return (fibo(i-1)+ fibo(i-2))
    

for i in range(n):
    print(fibo(i), end=" ")

end_time=time.time()
'''Iterative
print("Fibonacci Series is: 0 1", end=" ")
for i in range(0,n-2):
    sum=a+b
    print(final,end=" ")
    a=b
    b=final
'''
    
print("\nEnd time: ",end_time)
print("Total time taken for program to execute: ",end_time-start_time)

