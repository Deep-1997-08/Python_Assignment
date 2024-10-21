start=int(input('Please input the starting of the  '))
stop=int(input('Please input the end range '))
sum=0
for i in range(start,stop):
    if i%2==1:
        sum+=i

print(f'Sum of odd numbers: {sum}')
