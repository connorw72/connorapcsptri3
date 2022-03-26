class Factorial:
    def __call__(self, n):
        input = 1
        for i in range(1,n+1):
        # multiply the term by each value between 1 and n+1
        	input = input * i
        return input
      
def main():
  a = int(input("Factorial of:"))
  # input the number of what factorial the user wants
  printfactorial = Factorial()
  print(printfactorial(a))
  