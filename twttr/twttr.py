def main():
    text = input("Input: ")
    print(f"Output: {shorten(text)}")

def shorten(word):
    output = ""
    vowels = "aeiouAEIOU"
    for c in word:
        if c not in vowels:
            output += c
    return output

if __name__ == "__main__":
    main()
