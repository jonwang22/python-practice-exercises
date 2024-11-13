# Regex Matching and Replacing with Phone Numbers
import re

phone_number = input()

pattern = r"00"

if re.match(pattern, phone_number):
    phone_number = re.sub(pattern, "+", phone_number)
    print(phone_number)
else:
    print(phone_number)


# Regex using Metacharacters
word = input()

# For patterns, you need to enclose them with quotations ""
# or you can set a variable and set the pattern argument
# as a variable with a raw string.
# If you set a variable with a raw string it looks like this,
# pattern = r"^m..e$"
if re.match("^m..e$", word):
    print("Match")
else:
    print("No match")