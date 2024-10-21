def handel_index_error(l,n):
    try:
        result=l[n]
        print(f'The element at index {n}: {result}')
    except Exception as e:
        print(e)

l=[1,2,3,4,4,5,6,7]

index=int(input('Enter the index you want to print '))

handel_index_error(l,index)        