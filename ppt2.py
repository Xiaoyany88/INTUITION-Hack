import collections 
import collections.abc 
from pptx import Presentation
from pptx.util import Inches, Pt
from font_size import *
import requests
from bs4 import BeautifulSoup
from io import BytesIO

def new_slide(prs, text):
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    left = Inches(1)
    top = Inches(1)
    width = Inches(8)
    height = Inches(4)

    txBox1 = slide.shapes.add_textbox(left, top, width, height)
    tf1 = txBox1.text_frame
    tf1.text = text

    tf1.paragraphs[0].font.size = Pt(24)

    txBox1.text_frame.word_wrap = True
    txBox1.text_frame.auto_size = True

# searches the internet using "keyword" and returns the picture to be put in the slide
def newPicture(keyword):
    # url = f"https://www.google.com/search?q={keyword}&tbm=isch"
    try:
        url = bing_image_urls(keyword, limit=1)[0]
    except Image.AttributeError as e:
        print(e)
        return [None, None]

    # Send a request to the search URL and get the HTML response
    # headers = {"User-Agent": "Mozilla/5.0"}
    # response = requests.get(url, headers=headers)
    # soup = BeautifulSoup(response.content, "html.parser")

    # Find the first image in the search results and get its URL
    # img_url = soup.find("img")["src"]
    # print(img_url)

    # Download the image from the URL
    response = requests.get(url)
    img_data = response.content

    # Create an image object using BytesIO
    image = BytesIO(img_data)

    # Return the image object
    return image, url




