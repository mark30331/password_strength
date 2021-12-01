def main():
    #prompt the user for the password.
    password = input(str("Enter your password: "))

    # call the individual functions and store thier respective
    # results when the password variable is passed
    result_of_numbers = check_for_number(password)
    result_of_uppercase = check_for_uppercase(password)
    result_of_lowercase = check_for_lowercase(password)
    result_of_special_symbols = check_for_special_symbols(password)

    # A variable that would add up all the combinations.
    combinations = 0

    # if true, This password has a numerical size of n=10 (the number of digits possible).
    if result_of_numbers:
        combinations += 10

    #if true, This password has an uppercase size of n=26 (the number of uppercases possible).
    if result_of_uppercase:
        combinations += 26

    #if true, #if true, This password has a lowercase size of n=26 (the number of lowercases possible).
    if result_of_lowercase:
        combinations += 26

    #if true, This password has special characters size of n=32 (the number of special characters possible).
    if result_of_special_symbols:
        combinations += 32

    #this computes the total combinations raised to power of the password length
    if combinations:
        combinations **= len(password)

    #calls the bits function and passes the combinations and stores the result
    result_of_bit_strength = bits(combinations)

    #prints out the final results
    print("There are", combinations, "combinations")
    print("That is equivalent to a key of", result_of_bit_strength, "bits")

#function to check if password contains a number
def check_for_number(password):
    if len(password) == 0:
        return False
    return any(i.isdigit() for i in password)

#function to check if password contains uppercase
def check_for_uppercase(password):
    if len(password) == 0:
        return False
    return any(i.isupper() for i in password)

#function to check if password contains lowercase
def check_for_lowercase(password):
    if len(password) == 0:
        return False
    return any(i.islower() for i in password)

#function to check if password contains a special characters
def check_for_special_symbols(password):
    if len(password) == 0:
        return False
    return any(not i.isalnum() for i in password)

#function to calculate the bits
def bits(combinations):
    i = 1
    while True:
        temp = 2**i
        if temp > combinations:
            break
        i += 1

    return i-1
    
#call the main function to execute the program
main()
