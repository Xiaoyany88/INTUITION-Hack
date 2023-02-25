from pptx import Presentation
from pptx.util import Inches

prs = Presentation()

slide = prs.slides.add_slide(prs.slide_layouts[0])

title = slide.shapes.title
title.text = "Hello World!"

subtitle = slide.placeholders[1]
subtitle.text = "This is a subtitle"

# img_path = 'image.png'
# pic = slide.shapes.add_picture(img_path, Inches(1), Inches(3), height=Inches(2))

prs.save('example.pptx')