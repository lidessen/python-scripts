import sys
from utils import read_all, get_files


def process(dir):
    files = get_files(dir)
    for file in files:
        process_one(file)


def process_one(path):
    res = read_all(path)
    rows = res.split("\n")
    splited_rows = map(lambda x: x.split("\t"), rows)
    res = filter(lambda x: len(x) > 1 and len(x[1]) > 0, splited_rows)
    res = list(res)
    res_en = list(map(lambda x: x[0], res))
    res_zh = list(map(lambda x: x[1], res))
    print(res)

    with open("./output_en.txt", "a", encoding="utf-8") as file_en:
        file_en.write("\n".join(res_en))
    with open("./output_zh.txt", "a", encoding="utf-8") as file_zh:
        file_zh.write("\n".join(res_zh))


def main(argv=None):
    if argv is None:
        argv = sys.argv
    process(argv[1])


if __name__ == "__main__":
    main(sys.argv)