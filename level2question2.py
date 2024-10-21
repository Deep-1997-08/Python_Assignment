def unique_numbers(n):
    return list(set(n))

l1=input('Enter the list with spaces').split()
l1=[int(x) for x in l1]
result=unique_numbers(l1)

print(result)