#!/usr/bin/python
# coding=utf-8

import sys 


class ColorMaker:
    def __init__(self, file_in, file_out):
        self.input_path = file_in
        self.output_path = file_out

    def make(self):
        fout = open(self.output_path, 'w')
        with open(self.input_path) as f:
            for line in f:
                line = line.rstrip('\n')
                data_buffer = self._parse(line)
                if len(data_buffer) == 4:
                    color = self._get_color(data_buffer[3])    
                    new_line = line + ' ' + color +'\n'
                    fout.write(new_line)
        fout.close()
    
    def _parse(self, line):
        temp = line.split(" ")        
        return temp 

    def _get_color(self, feature):
        fea = float(feature)
        if fea > 1 or fea < -1:
            print "featur error"
            return ""

        color = ""
        if fea > 0:
            color_num = (1.0 - fea) * 255.0 
            color = "0 " + str(int(color_num)) + " 0\n"
        else:
            color_num = (fea + 1.0) * 255.0
            color = str(int(color_num)) + ' 0 0\n'
        return color


def useage():
    print "usage:"
    print "python *.python file_in file_out"
    

if __name__ == '__main__':
    if len(sys.argv) != 3:
        exit(-1)

    file_in = sys.argv[1]
    file_out = sys.argv[2]
    color_maker = ColorMaker(file_in, file_out)
    color_maker.make()
