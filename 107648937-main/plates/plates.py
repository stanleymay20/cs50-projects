def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[:2].isalpha():
        return False

    found_digit = False
    for c in s:
        if c.isdigit():
            if not found_digit and c == '0':
                return False
            found_digit = True
        elif found_digit and c.isalpha():
            return False

    if any(c in s for c in " .!?,:;"):
        return False

    return True


if __name__ == "__main__":
    main()
