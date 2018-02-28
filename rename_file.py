#encoding=utf-8
import os


def rename(path, names=[], numbers=[]):
    if len(names) == 0 or len(numbers) == 0 or len(names) != len(numbers):
        return
    i = 0
    j = 1
    front = 'straight_sword_'
    end = '.png'
    fileNames = os.listdir(path)
    for fileName in fileNames:
        if os.path.isdir(os.path.join(path, fileName)):
            continue
        os.rename(
            os.path.join(path, fileName),
            front + names[i] + '_' + str(j).zfill(2) + end)
        if j >= numbers[i]:
            i += 1
            j = 1
            continue
        j += 1


path = u'D:\\temp\\'
names = [
    'stand', 'run', 'catched', 'die', 'block', 'counterAtk', 'attacked',
    'standUp', 'jump', 'jumpLightAtk', 'jumpHeavyAtk', 'roll', 'clsRngAtk1',
    'clsRngAtk2', 'clsRngAtk3', 'midRngAtk1', 'midRngAtk2', 'midRngAtk3',
    'longRngAtk1', 'longRngAtk2', 'longRngAtk3', 'skill'
]
numbers = [2, 6, 1, 1, 1, 3, 3, 1, 5, 3, 3, 7, 6, 3, 5, 4, 4, 7, 4, 4, 8, 5]
rename(path, names, numbers)