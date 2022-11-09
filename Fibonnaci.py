'''
#Using recursion
def fibonacci(n):
	if n<=1:
		return n
	else:
		return(fibonacci(n-1) + fibonacci(n-2))

n = int(input('Enter a number '))

fibo_series = []

for i in range(0,n):
	fibo_series.append(fibonacci(i))
	
print(fibo_series)

'''

#Non Recursive
a=int(input("Enter the first number of the series "))
b=int(input("Enter the second number of the series "))
n=int(input("Enter the number of terms needed "))
print(a,b,end=" ")
while(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1
