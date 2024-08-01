#1

addition = 4 + 4 
substraction = 4-2
multiplication = 4 * 4
division = 4 / 2
modulo = 4 % 1
integer_division = 4 //1

#2
#Rectangle
def rectangle():
    global x, y
    x = int((input(' input width here: \n')),2)
    y = int((input('Input length here: \n ')),2)
    return x * y
global rrr
def rrr():
    return x * y

rectangle()
print(f'The area of the rectangle is {rrr()}')

#3

def rectangle():
    global x, y
    x = float(input('Input width here: \n'))
    y = float(input('Input length here: \n '))
    return x * y

# Define rrr as a separate function
def rrr():
    return x * y

# Call the rectangle function to initialize x and y
rectangle()
print(f'The area of the rectangle is {rrr():.2f}')

  
  
  
