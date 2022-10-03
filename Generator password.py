import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@#$%&*\/"


Use_for = lower_case + upper_case + number + symbols
lenght_for_pass = 8

password = "".join(random.sample(Use_for, lenght_for_pass))

print("Your password:", password)
