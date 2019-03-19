# -*- coding: UTF-8 -*-
import os


def main():
    path = os.getcwd() + '\ChangeCollisionGD'
    for file in os.listdir(path):
        if os.path.isdir(file) or file != 'Player.tscn':
            continue
        change_text(path, file)
        break


def change_text(path, file):
    key_word_1 = 'type="RectangleShape2D"'
    replace_word_1 = 'type="ConvexPolygonShape2D"'
    key_word_2 = 'extents = Vector2'
    replace_word_2 = 'points = PoolVector2Array( 0, -%d, %d, 0, %d, %d, -%d, %d, -%d, 0 )\n'
    new_lines = []

    with open(os.path.join(path, file), 'r', encoding='UTF-8') as tscn_file:
        for line in tscn_file.readlines():
            if line.find(key_word_1) != -1:
                line = line.replace(key_word_1, replace_word_1)

            if line.find(key_word_2) != -1:
                split_line = line.strip().replace('\n', '').split(' ')
                width = int(split_line[-3].rstrip(','))
                height = int(split_line[-2])
                line = (replace_word_2 % (height, width, width, height, width,
                                          height, width))

            new_lines.append(line)

    with open(
            os.path.join(path, 'new.tscn'), 'w', encoding='UTF-8') as new_file:
        new_file.writelines(new_lines)


if __name__ == '__main__':
    main()
