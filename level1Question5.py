factorial=int(input("Please enter the number "))
result=1
for i in range(factorial, 0, -1):
    result*=i
    
print(f'Factorial is {result}')