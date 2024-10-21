def sum_digits(n):
    while n>=10:
        n= sum(int(digit) for digit in str(n))
    return n

num=int(input("Enter the input number"))

Result=sum_digits(num)
print(f'Final Output: {Result}')
    