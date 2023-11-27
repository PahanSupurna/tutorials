#PART 1
# Write a program to display “FAIL” if the mark entered is less than 40, otherwise display “PASS”.

mark=0

mark=int(input("Enter your marks. "))

if mark>40:
    print("PASS")

else:
    print("FAIL")
    

#PART 2
#Write a program that checks whether a number is even or odd and then displays the appropriate message.

num=0

num=int(input("Enter a number. "))

if num%2==0:
    print("Its an even number")

else:
    print("Its an odd number")
