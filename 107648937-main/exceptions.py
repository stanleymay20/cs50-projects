def get_int():
    while True:
        try:
            x =int(input("Whats' x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break


print(f"x is {x}")
 