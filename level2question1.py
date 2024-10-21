l1=(input('Enter the first list')).split()
l2=(input('Enter the second list')).split()

l1 = [int(x) for x in l1]
l2= [int(x) for x in l2]

common_element=list(set(l1)&set(l2))

print(f'common element: {common_element}')