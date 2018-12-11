import hashlib
import os
import sys


def check_files(path):
    file_dict = {}
    if not os.path.exists(path):
        return
    for (root, dirs, files) in os.walk(path):
        for file in files:
            md5 = hashlib.md5()
            name = os.path.join(root, file)
            sys.stdout.write("扫描中 %s" % file)
            sys.stdout.flush()
            f = open(name, "rb")
            md5.update(f.read())
            hash_code = md5.hexdigest()
            md5_str = str(hash_code).lower()
            
            if md5_str not in file_dict.keys():
                file_dict[md5.hexdigest()] = [name]
            else:
                file_dict[md5.hexdigest()].append(name)
            sys.stdout.write("\r")
            sys.stdout.flush()
    sys.stdout.write("\r")
    sys.stdout.flush()
    count = 0
    for (key, value) in filter(lambda x: len(x[1]) > 1, file_dict.items()):
        print("重复[%d]：" % len(value))
        count += len(value)
        for file in value:
            print("%s" % file)
    print("\n扫描完成！共发现%d个重复文件" % count)


def list_file(path):
    if not os.path.exists(path):
        return
    for (root, dirs, files) in os.walk(path):
        for file in files:
            print(os.path.join(root, file))


def main(argv=None):
    if argv is None:
        argv = sys.argv
    check_files(argv[1])


if __name__ == '__main__':
    main(sys.argv)
