import sys
import os
from project_analyze import get_package_json, get_dependencies


def main(argv=None):
    if argv is None:
        argv = sys.argv
    path = os.path.join(argv[1], 'package.json')
    for item in get_dependencies(get_package_json(path)):
        print('%s: %s' % (item.name, item.version))


if __name__ == "__main__":
    main(sys.argv)