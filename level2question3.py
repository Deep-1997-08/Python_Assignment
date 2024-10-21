hash_map={}
res={}
subjects=['Physics','Chemistry','Biology','Mathematics','Computer']
for i in subjects:
    hash_map[i]=int(input(f"Enter Marks for {i}"))
    if hash_map[i] >= 90:
        res[i]='A'
    elif hash_map[i]>=80:
        res[i]='B'
    elif hash_map[i]>=70:
        res[i]='C'
    elif hash_map[i]>=60:
        res[i]='D'
    elif hash_map[i]>=40:
        res[i]='E'
    else:
        res[i]='F'

for i in subjects:
    print(f'{i}: Grade {res[i]}')
                