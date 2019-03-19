#encoding=utf-8
import os
import shutil


def main():
    delete_files()

    copy_files()

    rename_files()


def delete_files():
    for fileName in os.listdir(determination_path):
        if os.path.isdir(os.path.join(determination_path, fileName)):
            continue
        os.remove(os.path.join(determination_path, fileName))


def copy_files():
    for fileName in os.listdir(source_path):
        if os.path.isdir(os.path.join(source_path, fileName)):
            continue
        shutil.copyfile(
            os.path.join(source_path, fileName),
            os.path.join(determination_path, fileName))


def rename_files():
    i = 0
    j = 1
    front = 'player_sword_'
    end = '.png'

    for fileName in os.listdir(determination_path):
        if os.path.isdir(os.path.join(determination_path, fileName)):
            continue

        os.rename(
            os.path.join(determination_path, fileName),
            os.path.join(determination_path,
                         (front + names_list[i]['name'] + '_' + str(j).zfill(2) + end)))
        if j >= names_list[i]['num']:
            i += 1
            j = 1
            continue
        j += 1


source_path = u'D:\\workspace\\python\\gameTools\\renamePng\\src'
determination_path = u'D:\\workspace\\python\\gameTools\\renamePng\\tgt'
names_list = [
    {'name': 'idle', 'num': 4},
    {'name': 'run', 'num': 6},
    {'name': 'block', 'num': 1},
    {'name': 'counter_atk_pt_1', 'num': 5},
    {'name': 'counter_atk_pt_2', 'num': 6},
    {'name': 'jump', 'num': 6},
    {'name': 'light_atk_in_air', 'num': 3},
    {'name': 'heavy_atk_in_air', 'num': 7},
    {'name': 'roll', 'num': 6},
    {'name': 'light_atk_1', 'num': 5},
    {'name': 'light_atk_2', 'num': 4},
    {'name': 'light_atk_3', 'num': 4},
	{'name': 'heavy_atk_1', 'num': 5},
    {'name': 'heavy_atk_2', 'num': 8},
    {'name': 'skill', 'num': 4},
    {'name': 'suffered', 'num': 1},
    {'name': 'hit_hard', 'num': 1},
    {'name': 'catched', 'num': 1},
    {'name': 'die', 'num': 3}
]

if __name__ == '__main__':
    main()
