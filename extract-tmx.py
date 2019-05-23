# -*- coding:utf-8 -*-

from lxml import etree
import sys


def read(filename, lang):
    xml = etree.parse(filename)
    return xml.xpath("//tuv[@xml:lang='%s']/seg" % lang)


def write(content, path):
    file = open(path, 'w', encoding="utf-8")
    file.writelines(content)
    file.close()


def process(path, lang):
    res = read(path, lang)
    mapped = map(lambda x: x.text + "\n", res)
    listedMap = list(mapped)
    write(listedMap, "./%s.txt" % lang)


def main(argv=None):
    if argv is None:
        argv = sys.argv
    process(argv[1], "en")
    process(argv[1], "zh_CN")


if __name__ == "__main__":
    main(sys.argv)