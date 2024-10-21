def isAnagram(s: str, t:str) -> bool:
    charcount1, charcount2={}, {}

    if len(s)!=len(t):
        return False
        
    
    for i in range(len(s)):
        charcount1[s[i]]=1+charcount1.get(s[i],0)
        charcount2[t[i]]=1+charcount2.get(t[i],0)

    for c in charcount1:
        if charcount1[c] != charcount2.get(c,0):
            return False
    return True

string1=input("Enter the first input string ")
string2=input("Enter the second input string ")
result=isAnagram(string1,string2)
print(result)



    
            
    