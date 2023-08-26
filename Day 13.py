def generate_distinct_sums(nums):
    distinct_sums = set()
    subsets = [[]]

    for num in nums:
        new_subsets = [subset + [num] for subset in subsets]
        subsets.extend(new_subsets)

        for subset in subsets:
            distinct_sums.add(sum(subset))

    return list(distinct_sums)

# Get input from user
input_str = input("Enter a set of integers separated by spaces: ")
nums = list(map(int, input_str.split()))

result = generate_distinct_sums(nums)
print("Distinct sums:", result)
