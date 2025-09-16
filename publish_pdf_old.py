from fpdf import FPDF
import xml.etree.ElementTree as ET

a4_w_mm = 210
a4_h_mm = 297
a4_x_pd = 20
container_w = a4_w_mm - int(a4_x_pd * 2)

h1_index = 0
h2_index = 0
h3_index = 0

def h2(pdf, text, border=0):
    gap = a4_w_mm - container_w
    font_size = 14
    line_height = font_size // 3
    pdf.set_font("Arial", size=font_size, style="B")
    pdf.x = gap // 2
    pdf.multi_cell(container_w, line_height, txt=f'''{text.strip()}''', ln=True, border=border, align='L')
    pdf.ln()

def paragraph(pdf, text, border=0):
    gap = a4_w_mm - container_w
    font_size = 11
    line_height = 5
    pdf.set_font("Arial", size=font_size)
    pdf.x = gap // 2
    pdf.multi_cell(container_w, line_height, txt=text.strip(), ln=True, border=border, align='L')
    pdf.ln()

def ol(pdf, number, text, border=0):
    global last_tag
    gap = a4_w_mm - container_w
    font_size = 11
    line_height = 5
    pdf.set_font("Arial", size=font_size)
    pdf.x = gap // 2
    pdf.x += 4
    line = '. '.join(text.split('. ')[1:])
    if len(number) == 1: number_w = 6
    else: number_w = 8 
    pdf.cell(number_w, line_height, txt=f'{number.strip()}. ', border=border, align='L')
    pdf.multi_cell(container_w - 10, line_height, txt=text, ln=True, border=border, align='L')
    pdf.ln(2)
    last_tag = 'ol'

y_cur = 0
gap_image = 4
def pdf_image_left(pdf, href):
    global y_cur
    y_cur = pdf.y
    gap = a4_w_mm - container_w
    pdf.x = gap // 2
    pdf.image(href, w=container_w//2 - gap_image//2)
    last_tag = 'img'

def pdf_image_right(pdf, href):
    global y_cur
    pdf.y = y_cur
    gap = a4_w_mm - container_w
    pdf.x = (gap // 2) + container_w//2 + gap_image//2
    pdf.image(href, w=container_w//2 - gap_image//2)
    last_tag = 'img'
    pdf.ln()

pdf = FPDF()
pdf.add_page()

tree = ET.parse('calendar-enable.dita')
root = tree.getroot()
print(root.attrib)
if root.tag == 'task':
    for child in root:
        if child.tag == 'title':
            title_text = child.text
            h2(pdf, title_text)
            print(child.text)
        elif child.tag == 'taskbody':
            child_context = child[0]
            child_image = child_context[0]
            href = child_image.attrib['href']
            pdf_image_left(pdf, href)
            pdf_image_right(pdf, href)
            for step_i, step in enumerate(child[1]):
                cmd_text = step[0].text
                ol(pdf, str(step_i), cmd_text)
            result_text = child[2][0].text
            print(result_text)
            paragraph(pdf, result_text)

# for body in root.iter('body'):
    # print(body.tag)
    # print(body[0].text)

# print(root.findall('body')[0][0].text)
# tree.write('xml_file.xml')

pdf.output('test-map.pdf')

quit()

with open('test-map.ditamap') as f: ditamap = f.read()
ditamap_lines = ditamap.split('\n')
content = ''
for line in ditamap_lines:
    if 'topicref' in line:
        href = line.split('href="')[1].split('"')[0]
        with open(href) as f: topic = f.read()
        topic = '<topic' + topic.split('<topic')[1]
        content += topic + '\n'
    else:
        content += line + '\n'

font_size = 11
line_height = 5
pdf.set_font("Arial", size=font_size)
pdf.multi_cell(0, line_height, txt=content, ln=True, border=0, align='L')
pdf.ln()

