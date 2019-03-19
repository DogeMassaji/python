# -*- coding: UTF-8 -*-
import os
import sys
sys.path.append('D:\\workspace\\python\\utils\\')
import FilesUtils as FU

def main():
    global src_path
    global tgt_path
    path = os.path.dirname(os.path.abspath(__file__))
    src_path = path + '\\src\\'
    tgt_path = path + '\\tgt\\'

    for file_name in os.listdir(src_path):
        if os.path.splitext(file_name)[1] != '.tscn':
            continue

        update(file_name)
        break

def update(file_name):
    contents = None
    key_word = 'points = PoolVector2Array( '
    with open(os.path.join(src_path, file_name), 'r', encoding='UTF-8') as src_file:
        contents = src_file.readlines()

    with open(os.path.join(tgt_path, file_name), 'w', encoding='UTF-8') as tgt_file:
        for line in contents:
            l = line
            
            if l.find(key_word) != -1 and l.count(',') == 9:
                points = l.replace(key_word, '').replace(' )', '').replace('\n', '').split(', ')
                points = [int(p) for p in points]
                max_point = max(points)
                min_point = min(points)
                l = key_word

                for point in points:
                    if point == max_point:
                        p = str(point - 2)
                    elif point == min_point:
                        p = str(point + 2)
                    else:
                        p = str(point)
                    l += (p + ', ')

                l = l.rstrip(' ').rstrip(',') + ' )\t'
            
            tgt_file.write(l)

if __name__ == '__main__':
    main()
