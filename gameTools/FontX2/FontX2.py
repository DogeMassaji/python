# -*- coding: UTF-8 -*-
import os

PATH = os.path.dirname(os.path.abspath(__file__))

FILE_NAME = 'Font_SC32.fnt'

def main():
	with open(os.path.join(PATH, 'src', FILE_NAME), 'r', encoding='utf-8') as src_file:
		lines = src_file.readlines()

	with open(os.path.join(PATH, 'tgt', FILE_NAME), 'w', encoding='utf-8') as tgt_file:
		for line in lines:
			if line.find('info face') != -1:
				front_txt = line[:line.find('size=')]
				size = line[line.find('size='):line.find('bold=')]
				back_txt = line[line.find('bold='):]
				size_old_value = size.strip().replace('size=', '')
				size_new_value = str(int(size_old_value) * 2)
				size = size.replace(size_old_value, size_new_value)
				tgt_file.write(front_txt + size + back_txt)
				continue
			if line.find('common lineHeight') != -1:
				front_txt = line[:line.find('lineHeight=')]

				lineHeight = line[line.find('lineHeight='):line.find('base=')]
				lineHeight_old_value = lineHeight.strip().replace('lineHeight=', '')
				lineHeight_new_value = str(int(lineHeight_old_value) * 2)
				lineHeight = lineHeight.replace(lineHeight_old_value, lineHeight_new_value)

				base = line[line.find('base='):line.find('scaleW=')]
				base_old_value = base.strip().replace('base=', '')
				base_new_value = str(int(base_old_value) * 2)
				base = base.replace(base_old_value, base_new_value)

				scaleW = line[line.find('scaleW='):line.find('scaleH=')]
				scaleW_old_value = scaleW.strip().replace('scaleW=', '')
				scaleW_new_value = str(int(scaleW_old_value) * 2)
				scaleW = scaleW.replace(scaleW_old_value, scaleW_new_value)

				scaleH = line[line.find('scaleH='):line.find('pages=')]
				scaleH_old_value = scaleH.strip().replace('scaleH=', '')
				scaleH_new_value = str(int(scaleH_old_value) * 2)
				scaleH = scaleH.replace(scaleH_old_value, scaleH_new_value)

				back_txt = line[line.find('pages='):]
				tgt_file.write(front_txt + lineHeight + base + scaleW + scaleH + back_txt)
				continue
			if line.find('char id') == -1:
				tgt_file.write(line)
				continue

			fields = split_line(line)

			char_id = fields[0]

			x_old_value = fields[1].strip().replace('x=', '')
			x_new_value = str(int(x_old_value) * 2)
			x = fields[1].replace(x_old_value, x_new_value)[:len(fields[1])]
			
			
			y_old_value = fields[2].strip().replace('y=', '')
			y_new_value = str(int(y_old_value) * 2)
			y = fields[2].replace(y_old_value, y_new_value)[:len(fields[2])]
			
			width_old_value = fields[3].strip().replace('width=', '')
			width_new_value = str(int(width_old_value) * 2)
			width = fields[3].replace(width_old_value, width_new_value)[:len(fields[3])]
			
			height_old_value = fields[4].strip().replace('height=', '')
			height_new_value = str(int(height_old_value) * 2)
			height = fields[4].replace(height_old_value, height_new_value)[:len(fields[4])]

			xoffset = fields[5]
			yoffset = fields[6]
			
			xadvance_old_value = fields[7].strip().replace('xadvance=', '')
			xadvance_new_value = str(int(xadvance_old_value) * 2)
			xadvance = fields[7].replace(xadvance_old_value, xadvance_new_value)[:len(fields[7])]

			page = fields[8]
			chnl = fields[9]

			new_line = char_id + x + y + width + height + xoffset + yoffset + xadvance + page + chnl
			
			tgt_file.write(new_line)


def split_line(line):
	fields = []
	fields.append(line[0 : line.find('x=')])
	fields.append(line[line.find('x=') : line.find('y=')])
	fields.append(line[line.find('y=') : line.find('width=')])
	fields.append(line[line.find('width=') : line.find('height=')])
	fields.append(line[line.find('height=') : line.find('xoffset=')])
	fields.append(line[line.find('xoffset=') : line.find('yoffset=')])
	fields.append(line[line.find('yoffset=') : line.find('xadvance=')])
	fields.append(line[line.find('xadvance=') : line.find('page=')])
	fields.append(line[line.find('page=') : line.find('chnl=')])
	fields.append(line[line.find('chnl=') :])
	return fields


if __name__ == "__main__":
	main()