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
    front = 'hero_sword_'
    end = '.png'

    for fileName in os.listdir(determination_path):
        if os.path.isdir(os.path.join(determination_path, fileName)):
            continue

        os.rename(
            os.path.join(determination_path, fileName),
            os.path.join(determination_path,
                         (front + names[i] + '_' + str(j).zfill(2) + end)))
        if j >= numbers[i]:
            i += 1
            j = 1
            continue
        j += 1


source_path = u'D:\\temp\\'
determination_path = u'D:\\temp\\rename\\'
names = [
    'stand', 'run', 'block', 'counter_atk_pt_1', 'counter_atk_pt_2', 'jump',
    'light_atk_in_air', 'heavy_atk_in_air', 'roll', 'sprint_atk',
    'light_atk_1', 'combo_1', 'combo_2', 'heavy_atk', 'combo_3', 'skill_pt_1',
    'skill_pt_2', 'skill_pt_3', 'suffered', 'hit_hard', 'catched', 'die'
]
numbers = [4, 6, 1, 5, 5, 6, 3, 3, 6, 4, 5, 4, 4, 5, 8, 6, 3, 5, 1, 1, 1, 3]

if __name__ == '__main__':
    main()
