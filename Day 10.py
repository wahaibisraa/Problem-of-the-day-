def contains_elements_in_range(arr, A, B):
    for num in range(A, B + 1):
        if num not in arr:
            return False
    return True

input_array = list(map(int, input("Enter the array elements: ").split()))
A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
result = contains_elements_in_range(input_array, A, B)

if result:
    print("The array contains all elements in the range.")
else:
    print("The array does not contain all elements in the range.")
