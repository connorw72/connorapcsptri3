import w0.shipanimation
import w0.faceanimation
import w0.swap
import w0.keypad
import w0.tree
import w1.fibonacci
import w1.infodb

main_menu = [
    ["Swap", w0.swap.main],
    ["Keypad", w0.keypad.main],
    ["Tree", w0.tree.main]
]

animationsub_menu = [
    ["Ship Animation", w0.shipanimation.main],
    ["Face Animation", w0.faceanimation.main]
]
landlsub_menu = [
    ["InfoDB", w1.infodb.main],
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


def animationsubmenu():
    title = "Function Submenu" + banner
    buildMenu(title, animationsub_menu)
def landlsubmenu():
    title = "Function Submenu" + banner
    buildMenu(title, landlsub_menu)


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Animations", animationsubmenu])
    menu_list.append(["Lists and Loops", landlsubmenu])
    buildMenu(title, menu_list)


if __name__ == "__main__":
    menu()