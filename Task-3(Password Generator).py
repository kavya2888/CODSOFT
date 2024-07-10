# Password Generator
import random

# Lower Case Alphabets to be used in password
lowercase = "abcdefghijklmnopqrstuvwxyz"
# Upper Case Alphabets to be used in password
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Digits to be used in password
numbers   = "0123456789"
# Symbols to be used in password
symbols   = "!@#$%^&*()_+-={[]}|:;'<,.>?/"
# Combining all strings into a single string
string = lowercase + uppercase + numbers + symbols

length = int(input("Enter the desired length of password :"))

# Assigning password random strings of required length
password = ''.join(random.sample(string,length))

print("Your New Password :",password)