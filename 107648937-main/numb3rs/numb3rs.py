import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        octets = matches.groups()
        for octet in octets:
            if not 0 <= int(octet) <= 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
