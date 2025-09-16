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

image_num_cur = 0
y_cur = 0
gap_image = 2
def pdf_image_left(pdf, href):
    global y_cur
    y_cur = pdf.y
    gap = a4_w_mm - container_w
    pdf.x = gap // 2
    pdf.image(href, w=container_w//2 - gap_image//2)
    last_tag = 'img'
    print(image_num_cur)

def pdf_image_right(pdf, href):
    global y_cur
    pdf.y = y_cur
    gap = a4_w_mm - container_w
    pdf.x = (gap // 2) + container_w//2 + gap_image//2
    pdf.image(href, w=container_w//2 - gap_image//2)
    last_tag = 'img'
    pdf.ln(gap_image)

def gen():
    global image_num_cur
    pdf = FPDF()
    pdf.add_page()
    tree = ET.parse('tmp/map.ditamap')
    root = tree.getroot()
    if root.tag == 'map':
        for task in root:
            if task.tag == 'task':
                for child in task:
                    if child.tag == 'title':
                        title_text = child.text
                        h2(pdf, title_text)
                        print(child.text)
                    elif child.tag == 'taskbody':
                        child_context = child[0]
                        for child_image in child_context:
                            href = child_image.attrib['href']
                            if image_num_cur % 2 == 0:
                                pdf_image_left(pdf, href)
                            else:
                                pdf_image_right(pdf, href)
                            image_num_cur += 1
                        if image_num_cur % 2 == 1:
                            pdf.ln()
                        pdf.ln(gap_image)
                        image_num_cur = 0
                        for step_i, step in enumerate(child[1]):
                            cmd_text = step[0].text
                            ol(pdf, str(step_i+1), cmd_text)
                        result_text = child[2][0].text
                        print(result_text)
                        paragraph(pdf, result_text)
                pdf.ln(10)
    pdf.output('test-map.pdf')
