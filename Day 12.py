def alternate_positive_negative(arr):
    pos = [x for x in arr if x > 0]
    neg = [x for x in arr if x < 0]
    
    result = []
    i, j = 0, 0
    while i < len(pos) and j < len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i += 1
        j += 1
    
    while i < len(pos):
        result.append(pos[i])
        i += 1
    
    while j < len(neg):
        result.append(neg[j])
        j += 1
    
    return result

# Taking user input for array
N = int(input("Enter the size of the array: "))
arr = []
for _ in range(N):
    num = int(input("Enter a number: "))
    arr.append(num)

result_array = alternate_positive_negative(arr)
print("Array with alternate positive and negative numbers:", result_array)
