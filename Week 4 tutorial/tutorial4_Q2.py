
count=0
score=0
total=0
average=0

while score!=-9:
    score=float(input("Enter the score"))
    count+=1
    total+=score

average = total/count
print(average)

'''
def parse_int(s: str):
    is_valid = True 
    parsed_int=0

    while not is_valid:
        try:
            parsed_int = int(s) 
            is_valid = True 
            return parsed_int
        except ValueError:
            print("Enter a valid number")
        except ValueError:
            print("Enter a valid number")

    return parsed_int

user_input = input("Enter a number, or type -9 to quit")
'''