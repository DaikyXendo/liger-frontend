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
    command = ""
    is_open_command = False

    for char in text:
        if char == "<":
            is_open_tag = True
            is_open_command = False
            continue

        if is_open_tag:
            if char == ">":
                is_open_tag = False

                tag_type = (
                    "close"
                    if tag.startswith("/")
                    else "au_close"
                    if tag.endswith("/")
                    else "open"
                )

                name = tag.split(" ")[0].replace("/", "")

                print(tag_type, name, "<" + tag + ">")
                tag = ""
            else:
                tag += char
        else:
            if char == ":":
                name = command.strip().split(" ")[0]

                print("command", name, command + ":")
                command = ""

            else:
                command += char


if __name__ == "__main__":
    main()
