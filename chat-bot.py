import sys


def process_input(text):
    if text.find("?") != -1 or text.find("？") != -1:
        return "嗯嗯"
    return text


def main():
    while True:
        print(process_input(input()))


if __name__ == "__main__":
    main()