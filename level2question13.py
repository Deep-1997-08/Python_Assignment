def test_initial_character(l,n):
    
    start=lambda l,n: l.startswith(n)
    result=start(l,n)
    return result
    
    
s=input("Enter the input string ")
char=input("Enter the initial character ")
print(test_initial_character(s,char))