def find_median(n):
    sorted_list=sorted(n)
    
    n=len(sorted_list)
    
    if n%2 ==1:
        median=sorted_list[n//2]
    
    else:
        median=(sorted_list[(n//2)-1]+ sorted_list[n//2])/2
    
    return median

n=input("Enter the list").split()
n=[int(x) for x in n]
median=find_median(n)
print(median)