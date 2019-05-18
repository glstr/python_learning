#!/usr/bin/python
# coding:utf-8

import sys


def py_code_generator(file_name):
    f = open(file_name, "w")
    header = "#!/usr/bin/python\n# coding:utf-8\n\n\n"
    man_func = "if __name__ == '__main__':\n    exit(1)"
    f.write(header)
    f.write(man_func)
    f.close()
    return 


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(1)
    py_code_generator(sys.argv[1])

