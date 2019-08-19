import json


def get_package_json(file_path):
    with open(file_path, 'rt') as f:
        return json.load(f)


def get_dependencies(package_json):
    return list(
        map(lambda item: Dependency(item[0], item[1]),
            package_json['dependencies'].items()))


class Dependency:
    def __init__(self, name, version):
        self.name = name
        self.version = version
