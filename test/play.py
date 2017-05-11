"Wassup dogs"

def print_me(val):
    "Call sub func"
    def printer():
        "Print val"
        nonlocal val
        val += 2
        print(val)
    print(val)
    printer()
    print(val)

print_me(2)
