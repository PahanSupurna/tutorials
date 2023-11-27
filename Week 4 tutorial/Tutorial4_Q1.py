import random
user=0
hidden_num=random.randrange(1,20)

while True:
    user=int(input("Enter a number between 1 and 20. "))

    if 0<user<21:
        if user==hidden_num:
            print("Yes the random number is ",hidden_num)
            break
        elif abs(hidden_num-user)<5:
            print('Incorrect number but its so close. Please try again')
        elif abs(hidden_num-user)<10:
            print('Incorrect number but close. Please try again')
        elif abs(hidden_num-user)<15:
            print('Incorrect number and not close. Please try again')
        else:
            print('Incorrect number and its far away. Please try again')
            #this is just asking weather the random number is greater or less than our number so we can right it as,
            #print('greater' if hidden_num>user or 'less)
    else:
        print("Invalid input please check the answer") 

'''
hidden=6

user=int(input("Enter a number between 1 and 20. "))

while(int(user) != hidden):
    user=int(input("Enter a number between 1 and 20. "))
    print('{user} is an Incorrect number. Please try again')
    user=int(input("Enter a number between 1 and 20. "))

print("Yes the random number is ",hidden_num)
'''