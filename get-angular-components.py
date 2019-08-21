import sys
import os
import json
from utils import print_to_line, get_files, get_component_name


def main(argv=sys.argv):
    common_files = get_files(argv[1], r'[a-zA-Z0-9-]*\.component\.ts')
    ie_files = get_files(argv[1], r'[a-zA-Z0-9-]*\.ie\.component\.ts')
    ionic_files = get_files(argv[1], r'[a-zA-Z0-9-]*\.ionic\.component\.ts')

    common_conponents = get_component_name(common_files)
    ie_conponents = get_component_name(ie_files)
    ionic_conponents = get_component_name(ionic_files)

    print("[%s]\n" % ",".join(common_conponents))
    print("[%s]\n" % ",".join(ie_conponents))
    print("[%s]\n" % ",".join(ionic_conponents))


if __name__ == "__main__":
    main(sys.argv)