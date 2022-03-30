def findlcm(a, b):
    if (a > b):
        maximum = a
    else:
        maximum = b
    while (True):
        if (maximum % a == 0 and maximum % b == 0):
            break
        maximum = maximum + 1
    return maximum


class Lcm:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        if self.a > self.b:
            s = self.b

        if self.b > self.a:
            s = self.a

        while (True):
            if (s % self.a == 0 and s % self.b == 0):
                break
            s = s + 1
        return s


def tester():
    num = input("Imperative [I] or OOP [O]")
    try:
        if num == 'I':
            print("The LCM, Least Common Multiple, of 9 and 12 is : ", end="")
            print(findlcm(9, 12))
        elif num == 'O':
            L = Lcm(9, 12)
            print("The LCM, Least Common Multiple, of 9 and 12 is : ", end="")
            print(L())
    except:
        print("Sorry, try again!")


if __name__ == "__main__":
    tester()