# -*- coding: UTF-8 -*-
import os

PATH = os.path.dirname(os.path.abspath(__file__))

def main():
	with open(os.path.join(PATH, 'Key.txt'), 'r', encoding='UTF-8') as key_file:
		lines = key_file.readlines()

	with open(os.path.join(PATH, 'Output.txt'), 'w', encoding='UTF-8') as output_file:
		for line in lines:
			l = line.replace('\n', '')
			if len(l) == 0:
				continue
			split_strs = l.split(' ')
			temp_str = '{"code":"%s","name":"%s"},\n'
			output_file.write(temp_str % (split_strs[0], split_strs[1]))

if __name__ == '__main__':
	main()