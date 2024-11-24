# Create script, take in string, let me know how many vowels are in that string. Print a statement stating how many are in the string

# Take user input for string
user_string = input("What string do you want to use for this vowel checker? ") 

# iterate through string to identify vowels. have if statements checking if letter matches vowels if matches +1 count for vowels. 
# since i want to iterate through vowels, might use list

def vowel_checker(user_string):
    vowel_count = 0
    for letter in user_string.lower():
        if letter in ["a","e","i","o","u"]:
            vowel_count += 1
    return vowel_count

vowel_count = vowel_checker(user_string)

print(f"The number of vowels within your string is {vowel_count}.")