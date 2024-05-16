import os
import re


def read_file(path):
    with open(os.getcwd() + path, "r") as file:
        content = file.read()

    # Get content inside """
    pattern = r'UIML.*"""(.*)"""'

    matches = re.findall(pattern, content, re.DOTALL)
    if matches:
        text = " ".join(matches[0].split())

        return text

    return ""


def main():
    text = read_file("/src/main.py")

    tag = ""
    is_open_tag = False

    for char in text:
        if char == "<":
            is_open_tag = True
            continue

        if is_open_tag:
            if char == ">":
                is_open_tag = False

                tag_type = None
                if tag.startswith("/"):
                    tag_type = "close"
                elif tag.endswith("/"):
                    tag_type = "au_close"
                else:
                    tag_type = "open"

                name = tag.split(" ")[0]

                print(tag_type, name, "<" + tag + ">")
                tag = ""
            else:
                tag += char


if __name__ == "__main__":
    main()
