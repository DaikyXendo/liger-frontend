import os
import re


def read_file(path):
    with open(os.getcwd() + path, "r") as file:
        content = file.read()
        # Get content inside """
        pattern = r'UIML.*"""(.*)"""'

        matches = re.findall(pattern, content, re.DOTALL)
        text = " ".join(matches[0].split())

        return text


def main():
    text = read_file("/src/main.py")

    flag = "unknown"
    tag = ""
    is_close = False
    name = ""

    text_length = len(text)
    for idx, char in enumerate(text):
        next_char = text[idx + 1] if idx < text_length - 1 else None

        if is_close:
            is_close = False
            continue

        if flag == "unknown" and char == "<":
            flag = "close" if next_char == "/" else "open"

        if flag != "unknown" and next_char == ">":
            if char == "/":
                flag = "au_close"
                tag += "/>"
            else:
                tag += char + ">"

            print(flag, tag)
            flag = "unknown"
            tag = ""

            is_close = True
            continue

        tag += char


if __name__ == "__main__":
    main()
