def stone_piles(n):
    if n%2==0:
        start =2
    else:
        start =1 
        
    piles=[]
    while start<n:
        piles.append(start)
        start+=2
    
    return piles

n=int(input('Enter the input '))

result=stone_piles(n)

print(result)

