#!/usr/bin/python
# coding=utf-8

import sys


class DataFileAdaptor:
    def __init__(self, file_path):
        self.file_path = file_path
        return 

    def set_outputmodel(self, model):
        obj_array = model.split(" ") 
        if len(obj_array) != 0:
            self.obj_array = []
            for obj in obj_array:
                self.obj_array.append(int(obj) - 1)
            return True
        else:
            return False

    def output(self):
        output_file = file_path + ".ext"
        fout = open(output_file, "w")
        with open(file_path) as f:
            for line in f:
                res = self._ope_line(line)
                fout.write(res)
        fout.close()

    def _ope_line(self, line):
        line = line.rstrip('\n')
        data_array = line.split(" ")
        new_data = []
        for index in self.obj_array:
            new_data.append(data_array[index])
        sep = " "
        new_line = sep.join(new_data)
        new_line = new_line + "\n"
        return new_line

    def _read_file(self):
        return 


def usage():
    print "usage:"
    print "example"
    print "python " + sys.argv[0] + " file_name " + '"1 2 3"'
    return 


if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()
        exit()

    file_path = sys.argv[1]
    model = sys.argv[2]
    print file_path
    print model
    data_file_adaptor = DataFileAdaptor(file_path)
    ok = data_file_adaptor.set_outputmodel(model)
    if not ok:
        print "model error"
        exit()
    else:
        data_file_adaptor.output()

    
