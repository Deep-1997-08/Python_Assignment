n=int(input('Ernter the number to find out if it a perfect number or not '))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
    
if sum==n:
    print("Yes")
else:
    print('No')