import re
import sys

def main():
    html = input("HTML: ")
    print(parse(html))

def parse(s):
    # Regular expression for extracting YouTube embed URL
    matches = re.search(
        r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"',
        s,
        re.IGNORECASE
    )
    if matches:
        return f"https://youtu.be/{matches.group(1)}"
    return None

if __name__ == "__main__":
    main()
