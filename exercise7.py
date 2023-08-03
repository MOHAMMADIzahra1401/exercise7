import random 
n=int(input("Enter a number:"))
numbers=random.sample(range(1,n+10),n)
print(numbers)