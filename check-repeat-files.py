import hashlib
import os
import sys


def check_files(path):
    file_dict = {}
    files = get_all_files(path)
    progress = 0
    sys.stdout.write("\n")
    sys.stdout.flush()
    for fileName in files:
        md5 = hashlib.md5()
        f = open(fileName, "rb")
        md5.update(f.read())
        hash_code = md5.hexdigest()
        md5_str = str(hash_code).lower()
        
        if md5_str not in file_dict.keys():
            file_dict[md5.hexdigest()] = [fileName]
        else:
            file_dict[md5.hexdigest()].append(fileName)
        progress += 1
        sys.stdout.write("\r已扫描 [%d]" % (progress / len(files) * 100))
        sys.stdout.flush()
    sys.stdout.write("\r                ")
    sys.stdout.flush()
    count = 0
    for (key, value) in filter(lambda x: len(x[1]) > 1, file_dict.items()):
        print("重复[%d]：" % len(value))
        count += len(value)
        for file in value:
            print("     %s" % file)
    print("\n扫描完成！共发现%d个重复文件" % count)

def get_all_files(path):
    files = []
    if os.path.exists(path):
        for (root, dirs, files) in os.walk(path):
            for file in files:
                files.append(os.path.join(root, file))
    return files

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) > 1:
        check_files(argv[1])
    else:
        check_files(".")


if __name__ == '__main__':
    main(sys.argv)
