def can_reach_on_time(x):
    travel_time = 30  
    reach_time = x + travel_time  
    if reach_time <= 30:
        return "YES" 
    else:
        return "NO"  


x = int(input("Enter the value of X: "))
result = can_reach_on_time(x)
print("Chef will reach on time:", result)
