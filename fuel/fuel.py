def main():
    fraction = input("Fraction: ")
    try:
        percent = convert(fraction)
        print(gauge(percent))
    except (ValueError, ZeroDivisionError):
        pass


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
    except ValueError:
        raise ValueError
    percent = round(x / y * 100)
    return percent


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
