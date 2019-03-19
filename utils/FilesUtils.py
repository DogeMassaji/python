#encoding=utf-8
import os
import shutil

def delete_files(determination_path):
    for fileName in os.listdir(determination_path):
        if os.path.isdir(os.path.join(determination_path, fileName)):
            continue
        os.remove(os.path.join(determination_path, fileName))


def copy_files(source_path, determination_path):
    for fileName in os.listdir(source_path):
        if os.path.isdir(os.path.join(source_path, fileName)):
            continue
        shutil.copyfile(
            os.path.join(source_path, fileName),
            os.path.join(determination_path, fileName))