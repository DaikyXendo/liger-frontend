import os
import re


def main():
    with open(os.getcwd() + "/src/main.py", "r") as file:
        content = file.read()
        # Get content inside """
        pattern = r'UIML.*"""(.*)"""'

        matches = re.findall(pattern, content, re.DOTALL)
        text = " ".join(matches[0].split())

        flag = "unknown"
        tag = ""
        text_length = len(text)
        is_close = False
        name = ""
        for idx, char in enumerate(text):
            next_char = text[idx + 1] if idx < text_length - 1 else None

            if is_close:
                is_close = False
                continue

            if flag == "unknown" and char == "<":
                if next_char == "/":
                    flag = "close"
                else:
                    flag = "open"

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


main()
