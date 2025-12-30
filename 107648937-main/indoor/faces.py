def convert(emoticans):
    emoticon_map = {
        ":)":"🙂",
        ":(":"🙁",
    }
    for emoticon, uni_char in emoticon_map.items():
        emoticans = emoticans.replace(emoticon, uni_char)
    return emoticans


def main():
    emoticans = input("Enter a string with an emotican: ")
    converted_emotican= convert(emoticans)
    print("Hello", converted_emotican)


main()
