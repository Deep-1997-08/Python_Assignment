def twoSum (nums:list[int], target: int) -> int:
    prevMap={}
    count=0
    for i, n in enumerate(nums):
        diff=target - n
        if diff in prevMap:
            count+=1
        prevMap[n]=i
        
    return count

l1=input('Enter the list ').split()
l1=[int(x) for x in l1]
t=int(input('Enter the target '))

result=twoSum(l1,t)

print(result)