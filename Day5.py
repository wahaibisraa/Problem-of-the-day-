def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def count_fractions_with_sum_one(numerators, denominators):
    count = 0
    n = len(numerators)
    
    for i in range(n):
        for j in range(i + 1, n):
            num_sum = numerators[i] * denominators[j] + numerators[j] * denominators[i]
            den_sum = denominators[i] * denominators[j]
            common_divisor = gcd(num_sum, den_sum)
            
            if common_divisor == den_sum:
                count += 1
    
    return count

# Input
numerators = [int(x) for x in input("Enter numerators separated by spaces: ").split()]
denominators = [int(x) for x in input("Enter denominators separated by spaces: ").split()]

# Calculate and print the count of pairs
result = count_fractions_with_sum_one(numerators, denominators)
print("Count of pairs of fractions whose sum equals 1:", result)
