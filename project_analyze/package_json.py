import json


def get_package_json(file_path: str):
    with open(file_path, 'rt') as f:
        return json.load(f)


def get_dependencies(package_json: dict):
    return [
        Dependency(name, value)
        for name, value in package_json['dependencies'].items()
    ]


class Dependency:
    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version
