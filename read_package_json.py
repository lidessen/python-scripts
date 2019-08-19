import sys
from project_analyze import get_package_json, get_dependencies


def main(argv=None):
    if argv is None:
        argv = sys.argv
    for item in get_dependencies(get_package_json(argv[1])):
        print('%s: %s' % (item.name, item.version))


if __name__ == "__main__":
    main(sys.argv)