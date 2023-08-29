def is_power_of_2(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

N = int(input("Enter a non-negative integer: "))
if is_power_of_2(N):
    print(f"{N} - YES! , is a power of 2.")
else:
    print(f"{N} - NO! , is not a power of 2.")
