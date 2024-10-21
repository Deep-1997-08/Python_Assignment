def Count(s) -> bool:
    charcount1={}
        
    for i in range(len(s)):
        charcount1[s[i]]=1+charcount1.get(s[i],0)

    return charcount1

s=input("Enter the first input string ").split()

result=Count(s)
print(result)



    
            
    