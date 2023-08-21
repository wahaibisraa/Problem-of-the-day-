def count_equal_case_substrings(s):
    count = 0
    prefix_diff_count = {0: 1}  

    diff_count = 0  
    for char in s:
        if char.islower():
            diff_count += 1
        else:
            diff_count -= 1

        if diff_count in prefix_diff_count:
            count += prefix_diff_count[diff_count]

        if diff_count not in prefix_diff_count:
            prefix_diff_count[diff_count] = 0
        prefix_diff_count[diff_count] += 1

    return count

input_string = input("Enter a string: ")
result = count_equal_case_substrings(input_string)
print("Number of substrings:", result)
