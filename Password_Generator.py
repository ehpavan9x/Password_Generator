import random
import string

try:
    charectors = string.digits + string.ascii_letters + string.punctuation

    user_in = int(input("Enter the length of the Password: "))

    random_password = ''.join(random.choices(charectors, k=user_in))
except ValueError:

    print("Please enter only numbers")

finally:

    print(f"Your super strong password is : {random_password}")