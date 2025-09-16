topic_filename = ''
while True:
    topic_filename = input(f'ENTER FILENAME >> ')
    if topic_filename == '':
        topic_filename = 'topic-test'
        break
    elif ' ' in topic_filename:
        print(f'ERROR: Remove spaces')
    else:
        break

topic_id = ''
while True:
    topic_id = input(f'ENTER TOPIC ID >> ')
    if topic_id == '':
        break
    elif ' ' in topic_id:
        topic_id = ''
        print(f'ERROR: Invalid topic id. Topic id cannot contain spaces')
    else:
        break

xml = f'''
<?cml version="1.0" encoding="UTF-8"?>
<!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">

<concept id="{topic_id}">
    <title></title>
    <conbody>
        <p>
        </p>
    </conbody>
</concept>
'''.strip()
with open(f'{topic_filename}.dita', 'w') as f: f.write(xml)
