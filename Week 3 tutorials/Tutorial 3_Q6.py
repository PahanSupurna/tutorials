try:
    n = int(input('Give me a number over 100: ')) 
    if n <= 100:
     print(n, 'is not over 100')
except ValueError as v:
   print(f"Enter a valid integer: {v}")
