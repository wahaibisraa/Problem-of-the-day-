def can_buy_burgers(N, X, K):
    total_cost = N * X
    
    if total_cost <= K:
        return "YES"  
    else:
        return "NO"   


N = int(input("Enter the number of friends: "))
X = int(input("Enter the cost of each burger: "))
K = int(input("Enter the total amount Chef has: "))

result = can_buy_burgers(N, X, K)
print(result)
