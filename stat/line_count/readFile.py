from os import walk
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python", sys.argv[0], "path")
        exit(1)

    f = []
    for (dirpath, dirnames, filenames) in walk(sys.argv[1]):
        f.append([dirpath, filenames])

    for section in f:
        for file_name in section[1]:
            print(section[0]+'/'+file_name)
