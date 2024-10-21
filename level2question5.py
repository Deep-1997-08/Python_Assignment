def temperature_readings(l: list[int]):
    average= sum(l)/len(l)
    max_temp=max(l)
    min_temp=min(l)
    
    print(f'Average temperature: {average}')
    print(f'Minimum tempterature: {min_temp}')
    print(f'Maximum Temperature: {max_temp}')
    
l1=input("Enter the daily temperature with sapces").split()

l1=[int(x) for x in l1]

result=temperature_readings(l1)
