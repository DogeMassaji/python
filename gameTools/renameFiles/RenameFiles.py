# -*- coding: UTF-8 -*-
import os
import shutil


source_path = u'D:\\workspace\\python\\gameTools\\renameFiles\\src'
determination_path = u'D:\\workspace\\python\\gameTools\\renameFiles\\tgt'


def main():
    delete_files()

    copy_files()

    rename_files()


def delete_files():
    for file_name in os.listdir(determination_path):
        if os.path.isdir(os.path.join(determination_path, file_name)):
            continue
        os.remove(os.path.join(determination_path, file_name))


def copy_files():
    for file_name in os.listdir(source_path):
        if os.path.isdir(os.path.join(source_path, file_name)):
            continue
        shutil.copyfile(
            os.path.join(source_path, file_name),
            os.path.join(determination_path, file_name))


def rename_files():
    target_str = "Player"
    replace_str = "Enemy000"


    for file_name in os.listdir(determination_path):
        if os.path.isdir(os.path.join(determination_path, file_name)) or file_name.find(target_str) == -1:
            continue

        os.rename(
            os.path.join(determination_path, file_name),
            os.path.join(determination_path, file_name.replace(target_str, replace_str)))

if __name__ == '__main__':
    main()
