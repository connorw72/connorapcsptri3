def tree():
  height = int(input("Enter Height of Tree: "))
  for i in range(height):
    print((' ' * (height - i)) + ('*' * ((2 * i) + 1)))
  print((' ' * height) + '|')

def bottom(n):
    for x in range(3):
        for i in range(n-1):
            print(' ', end=' ')
        print('+ + +')
      
def main():
  tree()
