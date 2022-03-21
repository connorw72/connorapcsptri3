def recur_fibonacci(n):
   if n <= 1:
       return n
     # loops through n
   else:
       return(recur_fibonacci(n-1) + recur_fibonacci(n-2))
def display():
  terms = int(input("How many terms of the sequence do you want?"))
  try:
    # print fibonacci
    print("Fibonacci sequence:")
    for i in range(terms):
      print(recur_fibonacci(i))
  except:
    terms <= 0
    print("Plese enter a positive integer")