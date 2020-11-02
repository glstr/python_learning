#!/usr/bin/python
# coding=utf-8

import sys 


class ColorMaker:
    def __init__(self, file_in, file_out):
        self.input_path = file_in
        self.output_path = file_out
        self.colors = get_multi_colors_by_rgb([255,0,0], [0,255,255],100)

    def make(self):
        fout = open(self.output_path, 'w')
        with open(self.input_path) as f:
            for line in f:
                proc_func = self.get_process_func()
                new_line = proc_func(line)
                if new_line != "":
                    fout.write(new_line)
        fout.close()

    def get_process_func(self):
        # return self._default_process
        return self._new_process

    def _default_process(self, line):
        data_buffer = self._parse(line)
        new_line = ""
        if len(data_buffer) == 4:
            color = self._get_color(data_buffer[3])    
            new_line = line + ' ' + color +'\n'
        return new_line

    def _new_process(self, line):
        data_buffer = self._parse(line)
        if len(data_buffer) != 11:
            print len(data_buffer)
            print "parse err"
            return ""

        color_func = self.get_color_func()
        color = color_func(data_buffer[10])
        temp = (data_buffer[1], data_buffer[2], data_buffer[3], data_buffer[10], color)
        seq = ' '
        result = seq.join(temp)
        result = result + "\n"
        return result

    def _parse(self, line):
        # use for linux
        line = line.rstrip('\r\n')
        # use for unix
        # line = line.rstrip('\n')
        temp = line.split(" ")        
        return temp 

    def get_color_func(self):
        # return self._get_color_green
        return self.get_color_rgb

    def get_color_rgb(self, feature):
        fea = float(feature)
        if fea > 1 or fea < -1:
            print "featur error"
            return ""

        color_index = self._get_color_index(fea)
        color = self.colors[color_index]
        color_str = []
        for c in color:
            color_str.append(str(c))
        seq = ' '
        color = seq.join(color_str)
        return color

    def _get_color_green(self, feature):
        fea = float(feature)
        if fea > 1 or fea < -1:
            print "featur error"
            return ""

        color = ""
        if fea > 0:
            color_num = (1.0 - fea) * 255.0 
            color = "0 " + str(int(color_num)) + " 0"
        else:
            color_num = (fea + 1.0) * 255.0
            color = str(int(color_num)) + ' 0 0'
        return color

    def _get_color_index(self, fea):
        color_num = 0.0
        if fea > 0:
            color_num = (1.0 - fea) * 100.0 
        else:
            color_num = (fea + 1.0) * 100.0
        return int(color_num)


def get_multi_colors_by_rgb(begin_color, end_color, color_count):
    if color_count < 2:
        return []
    colors = []
    steps = [(end_color[i] - begin_color[i]) / (color_count - 1) for i in range(3)]
    for color_index in range(color_count):
        colors.append([int(begin_color[i] + steps[i] * color_index) for i in range(3)])
 
    return colors


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
