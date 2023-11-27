import random
count=0

dice1=0
dice2=0

for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)

    if dice1==dice2:
        count+=1
    
print('Out of 100 you rolled ',count,' doubles')