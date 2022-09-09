
def convert_100_to_celsius():
    # Convert a temperature of 100 degrees fahrenheit to celsius
    # Save this to a variable called celsius_100, and use print() to print out the value
    # Is the resulting temperature you get an integer or float?
    # Print 'float' if it is a float or 'int' if it is an int
    # How do you know? Write a comment below your code explaining how you know which it is
    fahr = 100
    celsius_100 = (fahr - 32) * 5 / 9
    print(celsius_100)
    print('float')
    # The number is a decimal number, not a whole number (because we multiply it by 5/9).

def convert_0_to_celsius():
    # Convert a temperature of 0 degrees fahrenheit to celsius
    # Save this to a variable called celsius_0, and use print() to print out the value
    fahr = 0
    celsius_0 = (fahr - 32) * 5 / 9
    print(celsius_0)

def convert_34_2_to_celsius():
    # Convert a temperature of 34.2 degrees fahrenheit to celsius
    # Do this one all in one print statement without saving any variables
    print( (34.2 - 32) * 5 / 9)

'''
Now, can you convert back?
'''

def convert_5_to_fahrenheit():
    # Convert a temperature of 5 degrees celsius to fahrenheit and print it out
    cels = 5
    fahr_5 = (cels * (9/5)) + 32
    print(fahr_5)

def hotter_temp():
    # What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
    # Print out the hotter temp: '30.2 degrees celsius' or '85.1 degrees fahrenheit', respectively
    if ((30.2 * 9/5) + 32) > 85.1:
        print('30.2 degrees celsius')
    elif ((30.2 * 9/5) + 32) < 85.1:
        print('85.1 degrees fahrenheit')
    else:
        print('30.2 degrees celsius is equal to 85.1 degrees fahrenheit')

