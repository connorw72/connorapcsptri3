import w0.shipanimation
import w0.faceanimation
import w0.swap
import w0.keypad
import w0.tree
import w1.fibonacci
import w1.infodb
import w2.factorial
import w2.math
import w2.palindrome
import w2.lcm
import w3.paint

from time import sleep
import sys
welcome = "Welcome to Connor's Menu"
def yo():
  for x in welcome:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.1)

main_menu = [
    ["InfoDB", w1.infodb.main],
]

artsub_menu = [
    ["Ship Animation", w0.shipanimation.main],
    ["Face Animation", w0.faceanimation.main],
    ["Tree", w0.tree.main],
    ["Waterfall", w3.paint.water],
    ["Clouds", w3.paint.clouds],
    ["Rainbow", w3.paint.rain]
]

mathsub_menu = [
    ["Factorial", w2.factorial.main],
    ["Greatest Common Denominator", w2.math.gcd],
    ["Palindrome", w2.palindrome.main],
    ["LCM", "w2/lcm.py"],
    ["Swap", w0.swap.main],
    ["Keypad", w0.keypad.main],
    ["Fibonacci", w1.fibonacci.display]
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op
    for key, value in prompts.items():
        print(key, '->', value[0])
    choice = input("Type your choice> ")
    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")
    buildMenu(banner, options)


def artsubmenu():
    title = "Function Submenu" + banner
    buildMenu(title, artsub_menu)
def mathsubmenu():
    title = "Function Submenu" + banner
    buildMenu(title, mathsub_menu)

def menu():
    title = "!" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Art", artsubmenu])
    menu_list.append(["Math", mathsubmenu])
    buildMenu(title, menu_list)


if __name__ == "__main__":
    yo()
    menu()