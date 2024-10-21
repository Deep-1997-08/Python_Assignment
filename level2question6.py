def is_divisible_by_two(n):
    if n==1:
        return True
    
    if n<1 or n%2!=0:
        return False
    
    return is_divisible_by_two(n//2)

number=int(input("Enter the number"))

result=is_divisible_by_two(number)
print(result)