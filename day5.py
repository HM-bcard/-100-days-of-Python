# 1.
def program_1():
    user_input = int(input('please input an integer number here: \n'))
    if user_input % 2 == 0:
        print('This is an even number')
    else:
        print('This is an odd number')

  #2.
  def program_2():
    user_input1 = int(input("Please input an integer number below: \n"))
    user_input2 = int(input("Please input an integer number below, other than the previous one: \n"))
    user_input3 = int(input("Please input an integer number below, other than the previous one: \n"))
    if user_input1 >= user_input2 and user_input1 >= user_input3:
        print(f"The highest number is {user_input3}" )
    elif user_input2 >= user_input1 and user_input1 >= user_input3:
        print(f"The highest number is {user_input3}" )
    elif user_input3 >= user_input1 and user_input3 >= user_input2:
        print(f"The highest number is {user_input3}" )
    else:
        print('There seems to be an error')


#3.
year = int(input('Input the year here to check whether it's a leap year:\n'))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")   
else:
  print("Not leap year")

  #4.
percentage = int(input('Provide the percentage here:'))

if percentage > 90:
  print('it\'s an "A" ')
elif percentage > 80:
  print('it\'s a \'B\'')
elif percentage > 70:
  print('it\'s a \'C\'') 
elif percentage > 60:
  print('it\'s a \'D\'')
elif percentage > 50:
  print('it\'s an \'E\'')
elif percentage <= 50:
  print('it\'s an \'F\'')
  
