def tree():
  height = int(input("Enter Height of Tree: "))
  for i in range(height):
    print((' ' * (height - i)) + ('*' * ((2 * i) + 1)))
  print((' ' * height) + '|')

def main():
  tree()