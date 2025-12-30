import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    matches = re.search(
        r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$",
        s
    )
    if not matches:
        raise ValueError("Invalid format")

    h1, m1, period1, h2, m2, period2 = matches.groups()

    h1 = int(h1)
    h2 = int(h2)
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    if not (1 <= h1 <= 12) or not (1 <= h2 <= 12):
        raise ValueError("Invalid hour")
    if not (0 <= m1 < 60) or not (0 <= m2 < 60):
        raise ValueError("Invalid minutes")

    h1_24 = to_24_hour(h1, period1)
    h2_24 = to_24_hour(h2, period2)

    return f"{h1_24:02}:{m1:02} to {h2_24:02}:{m2:02}"

def to_24_hour(hour, period):
    if period == "AM":
        return hour % 12
    else:
        return (hour % 12) + 12

if __name__ == "__main__":
    main()
