def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    user_text = input("Input: ")
    output = convert(user_text)
    print(output)


main()
