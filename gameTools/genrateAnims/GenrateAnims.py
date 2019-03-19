# -*- coding: UTF-8 -*-
import os

ext_resource_str = '[ext_resource path="res://resources/texture/hero/heroWithSword/hero_sword.sprites/%s.tres" type="Texture" id=%d]\n'

anim_config_str = '''[sub_resource type="Animation" id=%d]

resource_name = "%s"
length = %.2f
loop = false
step = 0.04
tracks/0/type = "value"
tracks/0/path = NodePath("Player_Sprite:texture")
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

node_anim_list_str = 'anims/%s = SubResource( %d )\n'


def main():
    path = os.getcwd()
    files_list = os.listdir(path)
    anim_list_1 = []
    anim_list_2 = []
    anim_set = []
    for file in files_list:
        if os.path.splitext(file)[1] == '.png':
            anim_png_name = os.path.splitext(file)[0]
            anim_list_1.append(anim_png_name)
            anim_name = anim_png_name[:-3].replace('hero_sword_', '')
            anim_list_2.append(anim_name)
            if not anim_name in anim_set:
                anim_set.append(anim_name)

    with open(
            os.path.join(path, 'ext_resource.txt'), 'w',
            encoding='UTF-8') as ext_resource_file:
        for i in range(len(anim_list_1)):
            ext_resource_file.write(ext_resource_str % (anim_list_1[i], i + 2))

    with open(
            os.path.join(path, 'anim_config.txt'), 'w',
            encoding='UTF-8') as anim_config_file:
        step = 0.04

        for i in range(len(anim_set)):
            resource_name = anim_set[i]
            count = anim_list_2.count(resource_name)
            id = i + 1
            length = 2 * step * count
            times = ''
            transitions = ''
            values = ''
            for j in range(count):
                time = ('%.2f, ' % (2 * j * step))
                if time[0] == '0' and time[2] == '0' and time[3] == '0':
                    time = '0, '
                times += time
                transitions += '1, '
                ext_id = anim_list_2.index(resource_name) + 2 + j
                values += 'ExtResource( %d ), ' % ext_id
            times = times.rstrip().rstrip(',')
            transitions = transitions.rstrip().rstrip(',')
            values = values.rstrip().rstrip(',')

            anim_config_file.write(anim_config_str % (
                id, resource_name, length, times, transitions, values) + '\n')

    with open(
            os.path.join(path, 'node_anim_list.txt'), 'w',
            encoding='UTF-8') as node_anim_list_file:
        for i in range(len(anim_set)):
            node_anim_list_file.write(node_anim_list_str % (anim_set[i],
                                                            i + 1))


if __name__ == '__main__':
    main()