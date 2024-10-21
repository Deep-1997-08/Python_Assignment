s=input("Enter the input string")
letter=0
numbers=0
for i in s:
    if i.isalpha():
        letter+=1
    elif i.isdigit():
        numbers+=1
    else:
        break


print(f'Alphabets:{letter} & Numbers:{numbers}')