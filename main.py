import os
import xml.etree.ElementTree as ET

import publish_pdf

proj = 'aurora'

def map_gen_old(map_filepath):
    with open(map_filepath) as f: map_xml = f.read()
    print(map_xml)
    tree = ET.parse(map_filepath)
    root = tree.getroot()
    if root.tag == 'map':
        for child in root:
            if child.tag == 'topicref':
                child_href = child.attrib['href']
                child_type = child.attrib['type']
                print(child_href)
                print(child_type)

def map_gen(map_filepath):
    map_xml_output = ''
    with open(map_filepath) as f: map_xml = f.read()
    lines = map_xml.split('\n')
    for line in lines:
        if line.strip().startswith('<topicref '):
            tmp = line
            tmp = tmp.strip().split('href="')[1]
            tmp = tmp.strip().split('" ')[0]
            with open(tmp) as f: topic_xml = f.read()
            for topic_line in topic_xml.split('\n'):
                if topic_line.strip().startswith('<?cml '): continue
                if topic_line.strip().startswith('<!DOCTYPE '): continue
                map_xml_output += '    ' + topic_line + '\n'
        else:
            map_xml_output += line + '\n'
    return map_xml_output

maps_folderpath = f'projects/{proj}/maps'
maps_filepaths = [f'{maps_folderpath}/{filename}' for filename in os.listdir(maps_folderpath)]
for map_filepath in maps_filepaths:
    map_xml_expand = map_gen(map_filepath)
    print(map_xml_expand)
    with open('tmp/map.ditamap', 'w') as f: f.write(map_xml_expand)
    publish_pdf.gen()
