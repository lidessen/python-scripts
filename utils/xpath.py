from lxml import etree

def funcname(fileName):
    file = open(fileName)
    content = file.read()
    xml = etree.XML(content)
