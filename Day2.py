#User should enter array of numbers and you are giving the number, one of the two numbers that equals the sum of the given number. 

def find_number_equals(nums, target):
    num_set = set()
    result = []

    for num in nums:
        complement = target - num
        if complement in num_set:
            result.append((num, complement))
        num_set.add(num)

    return result


input_nums = input("Enter an array of numbers: ")
nums = [int(num) for num in input_nums.split(",")]

target = int(input("Enter the target number: "))

equals = find_number_equals(nums, target)

if equals:
    print("equals found:")
    for pair in equals:
        print(pair[0], pair[1])
else:
    print("No equals found.")
