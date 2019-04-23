import sys
import getopt
import os
from utils import print_to_line


def get_files(path='./'):
    result = []
    if os.path.exists(path):
        for (root, dummy, files) in os.walk(path):
            for file in files:
                result.append(os.path.join(root, file))
    return result


def __main__(argv=sys.argv):
    if (len(argv) > 1):
        print_to_line(get_files(argv[1]))
    else:
        print_to_line(get_files())


if __name__ == "__main__":
    __main__()
