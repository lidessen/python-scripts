import sys
from utils import read_lines


def process(path, count=2990000):
    res = read_lines(path, count)
    file = open("./output.txt", "w", encoding="utf-8")
    file.writelines(res)
    file.close()
    

def main(argv=None):
    if argv is None:
        argv = sys.argv
    process(argv[1])


if __name__ == "__main__":
    main(sys.argv)