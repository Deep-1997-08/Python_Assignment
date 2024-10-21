n1=int(input('Enter the first number'))
n2=int(input("Enter the second number"))

a, b = n1, n2

while b!=0:
    a,b = b, a%b
    
gcd=a

lcm =abs(n1*n2)//gcd

print(lcm)