import re
while True:
    password = input("Enter your password: ")

    length_check = len(password) >= 8
    digit_check = re.search(r"\d", password)
    uppercase_check = re.search(r"[A-Z]", password)
    special_char_check = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    if length_check and digit_check and uppercase_check and special_char_check:
        print("Strong Password")
        break   
    else:
        print("Weak Password. Try again!\n")