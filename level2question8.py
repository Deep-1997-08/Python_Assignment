def number_of_vowels(n):
    s=set('aeiou')
    count=0
    for i in n:
        if i in s:
            count+=1
            
    return count

s=input('Enter the sentence')
result=number_of_vowels(s)

print(result)