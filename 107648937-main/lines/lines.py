import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(sys.argv[1]) as file:
            count = 0
            for line in file:
                # Strip leading spaces
                stripped = line.lstrip()

                # Skip blank lines and comments (starts with "#")
                if stripped.startswith("#") or stripped == "":
                    continue

                # Count this as a line of code
                count += 1

            print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
