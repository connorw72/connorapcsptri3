def findgcd(num1, num2):
    if num1 == 0:
        return num1
    while num2 != 0:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1

class gcd:
  def __init__(self,n1,n2):
    self.n1 = n1
    self.n2 = n2
  def __class__(self):
    if n1 == 0:
      self.n1 = n1
    if n1 > n2:
      self.n1 = n1 - n2
    if n2 > n1:
      self.n2 = n2 - n1
    return n1



def gcd():
    a = int(input(" Enter the First Value for GCD: "))
    b = int(input(" Enter the Second Value for GCD: "))
    gcd = findgcd(a, b)
    print("\n GCD of {0} and {1} is: {2}".format(a, b, gcd))
    print() 