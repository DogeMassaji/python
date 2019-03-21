# -*- coding: UTF-8 -*-
import os
import json
import time

path = os.path.dirname(os.path.abspath(__file__))
'''
%1: resources_path
%2: tres_name
'''
ext_resource_str = '[ext_resource path="res://%s/%s" type="Texture" id=%d]\n'
'''
%1: id
%2: anim_name
%3: anim_length
%4: node_path
%5: times
%6: transitions
%7: ext_resource
'''
anim_config_str = '''[sub_resource type="Animation" id=%d]
resource_name = "%s"
length = %.2f
loop = false
step = 0.04
tracks/0/type = "value"
tracks/0/path = NodePath("%s")
tracks/0/interp = 1
tracks/0/loop_wrap = true
tracks/0/imported = false
tracks/0/enabled = true
tracks/0/keys = {
"times": PoolRealArray( %s ),
"transitions": PoolRealArray( %s ),
"update": 0,
"values": [ %s ]
}\n'''
'''
%1: anim_name
%2: id
'''
node_anim_list_str = 'anims/%s = SubResource( %d )\n'

current_time = time.strftime('%Y%m%d%H%M%S')


def main():
    input_json = read_input()
    anim_map = get_anim_map(input_json)

    os.mkdir(os.path.join(path, 'output', current_time))

    gen_ext_resource_txt(input_json, anim_map)

    gen_sub_resource_txt(input_json, anim_map)

    gen_anim_node_txt(anim_map)


def read_input():
    with open(
            os.path.join(path, 'input.json'), 'r',
            encoding='UTF-8') as json_file:
        return json.load(json_file)


def get_anim_map(input_json):
    files_list = os.listdir(os.path.join(path, 'input'))
    anim_name_list = []
    anim_map = []

    for file in files_list:
        if os.path.splitext(file)[1] == input_json['res_file_format'][
                'suffix']:
            anim_name = os.path.splitext(file)[0][:-3].replace(
                input_json['res_file_format']['prefix'], "")
            anim_name = to_big_hump(anim_name)
            if anim_name not in anim_name_list:
                anim_name_list.append(anim_name)
                anim_map.append({
                    'anim_name': anim_name,
                    'anim_file_list': [file]
                })
            else:
                anim_map[-1]['anim_file_list'].append(file)
    return anim_map


def to_big_hump(anim_name):
    name_part_list = anim_name.split('_')
    ret = ''
    for i in range(len(name_part_list)):
        ret += name_part_list[i].title()
        print()
    return ret


def gen_ext_resource_txt(input_json, anim_map):
    with open(
            os.path.join(path, 'output', current_time, 'ext_resource.txt'),
            'w',
            encoding='UTF-8') as ext_resource_file:
        id = 0
        for i in range(len(anim_map)):
            anim_file_list = anim_map[i]['anim_file_list']
            for j in range(len(anim_file_list)):
                id += 1
                ext_resource_file.write(ext_resource_str %
                                        (input_json['resources_path'],
                                         anim_file_list[j], id))


def gen_sub_resource_txt(input_json, anim_map):
    with open(
            os.path.join(path, 'output', current_time, 'sub_resource.txt'),
            'w',
            encoding='UTF-8') as sub_resource_file:
        step = 0.04
        id = 0

        for i in range(len(anim_map)):
            resource_name = anim_map[i]['anim_name']
            count = len(anim_map[i]['anim_file_list'])
            length = 2 * step * count
            times = ''
            transitions = ''
            values = ''
            for j in range(count):
                id += 1
                time = ('%.2f, ' % (2 * j * step))
                if time[0] == '0' and time[2] == '0' and time[3] == '0':
                    time = '0, '
                times += time
                transitions += '1, '
                values += 'ExtResource( %d ), ' % id
            times = times.rstrip().rstrip(',')
            transitions = transitions.rstrip().rstrip(',')
            values = values.rstrip().rstrip(',')

            sub_resource_file.write(anim_config_str % (
                i + 1, resource_name, length, input_json['node_path'], times,
                transitions, values) + '\n')


def gen_anim_node_txt(anim_map):
    with open(
            os.path.join(path, 'output', current_time, 'anim_node.txt'),
            'w',
            encoding='UTF-8') as anim_node_file:
        for i in range(len(anim_map)):
            anim_node_file.write(node_anim_list_str % (anim_map[i]['anim_name'],
                                                       i + 1))


if __name__ == '__main__':
    main()