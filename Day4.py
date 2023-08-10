"""
Mohammed wanted to find out if the person he was talking to online was a girl or a boy by their username by this method:
Charters in the username is single (user is a boy)otherwise it is girl.
"""

def guess_gender(username):
    num_chars = len(username)
    if num_chars == 1:
        return "Boy"
    else:
        return "Girl"
    
username = input("Enter the username: ")

gender = guess_gender(username)
print(f"The gender is: {gender}")
