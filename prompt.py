
# variable names in python have underscores
# snake_case
user_name = input("What is your name? ")

# in JavaScript we would write userName
#camelCase

#string substitution has 3 parts
# 1. a string...with placeholders
# 2. The subsitution operator
# 3. Values to interpolating into the string
#   Values should be in parens, separated by commas.
# greeting = "Hello, %s!" % (user_name,)
# print(greeting)

# if interpolating a single value,
# you dont need the parens or the comma

# print("Hello,", user_name, "!")
# print(user_name)

greeting = f"Hello, {user_name}!" 
print(greeting)