input = input("Please enter the string: ")

reverse = input[::-1]
if reverse.lower() == input.lower():
    print(input, " is a panlindrome")