class Palindrome:
    def __init__(self, test):
        self.test = test
    def __call__(self):
        test_strip = list([n for n in self.test if n.isalpha() or n.isnumeric()])
        self.test = "".join(test_strip)
        self.test = self.test.lower()
        #Test to see if the phrase/word is a palindrome
        if self.test == self.test[::-1]:
            return "is a palindrome"
        else:
            return "is not a palindrome"
# Testing these to see if they are palindromes
test_cases = ["A man, a plan, a canal -- Panama",  "racecar", "broncos", "r%ace /!@# ca%r", "#Heyyo!#!"]
badchar = " !@#$%^&*()/~|"

#good job factoring out if it has abd char or not, not exactly sure how you did though since you never explicitly remove
def main():
  try:
      for v in test_cases:
        palindrome = Palindrome(test=v)
        print(v, palindrome())
  except: 
    print("ERROR!")
    