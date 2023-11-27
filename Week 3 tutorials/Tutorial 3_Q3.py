#PART 1 -> Temperature Program

user_temp=0
user_selection=0

user_temp=int(input("Please enter the temperature that you want to convert. "))
user_selection=int(input("If you want to convert from Celsius to Fahrenheit, enter 1. \n If you want to convert from Fahrenheit to Celsius, please enter 2. "))

if user_selection==1 or 2:
    if user_selection==1:
        temp=(user_temp*1.8)+32
        print(f"Converted temperature is {temp} Fahrenheits.")

    else:
        temp=(user_temp-32)/1.8
        print(f"Converted temperature is {temp} Celsius.")
else:
    print("Please enter a number between 1 or

          
#PART 2 -> CALCULATOR ----------------------------------------------------------------------
add='+'
sub='-'
mul='*'
div='/'

num1=int(input("What is the first number? "))
num2=int(input("What is the second number? "))
operator=input("What is the operator")

if operator=='+':
    total=num1+num2

elif operator=='-':
    total=num1-num2

elif operator=='*':
    total=num1*num2

elif operator=='/':
    total=num1/num2

else:
    print("Please enter one of following 4 operators --> + , - , * , /. ")

print(f'The total is {total}')


#PART 3 -> TIP CALCULATOR --------------------------------------------------------------------

cost=int(input("Please enter the cost of the meal. "))

satisfaction=int(input("Please enter your satisfaction level.\n 1 ->  totaly satisfied \n 2 -> satisfied \n 3 -> desatisfied \n"))

try:
    if satisfaction==1:
        tip=cost*20/100

    elif satisfaction==2:
        tip=cost*15/100

    else: 
        tip=cost*10/100

    print(f"Satisfaction level -> {satisfaction}. \ntip = {tip}.")

except ValueError as V:
    print(f"{v}. Please enter 1 or 2 or 3 as your satisfied level.")
