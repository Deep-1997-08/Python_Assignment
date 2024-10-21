n=int(input('Enter any number'))

if n % 3 == 0 and n % 5 !=0:
    print('Consultadd') 
elif n % 3 != 0 and n % 5 ==0:
    print('Python Training')
elif n %3 ==3 and n % 5 ==0:
    print("Consultadd - Python Training")
else:
    print('Not divisible by both')