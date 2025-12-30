def main():

    # Output using our own function
    name = input("What's your name? ")
    hello(name)
    hello()


# Create our own function
def hello(to="world"):
    print("hello", to)


main()
