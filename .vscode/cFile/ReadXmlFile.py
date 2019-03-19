# -*- coding: UTF-8 -*-
import os
import xml.etree.ElementTree as ET

path = os.path.dirname(os.path.abspath(__file__))

def main():
	for file_name in os.listdir(path):
		if os.path.isdir(os.path.join(path, file_name)) or os.path.splitext(file_name)[1] != '.xml':
			continue

		readXmlFile(file_name)
		break

def readXmlFile(file_name):
	et = ET.parse(os.path.join(path, file_name))
	form_validation_el = et.getroot().find('form-validation')
	print(form_validation_el)



	temp = root.getElementsByTagName('form-validation')
	print(temp)

if __name__ == "__main__":
	main()
