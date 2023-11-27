yes_inputs=['yes','y']
no_inputs=['no','n']

like=input("Do you like python? (yes/no)")

like=like.lower()

if like in yes_inputs:
    print("You are on the right course.")
elif like in no_inputs:
    print("You might change your mind.")
else:
    print("I did not understand.")
