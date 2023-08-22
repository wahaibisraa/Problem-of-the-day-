def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

def longest_palindromic_substring(s):
    longest = ""
    for i in range(len(s)):
        palindrome1 = expand_around_center(s, i, i)
        if len(palindrome1) > len(longest):
            longest = palindrome1
        
       
        palindrome2 = expand_around_center(s, i, i + 1)
        if len(palindrome2) > len(longest):
            longest = palindrome2
    
    return longest

# Example 
input_string = "civic deified "
result = longest_palindromic_substring(input_string)
print(result)  
