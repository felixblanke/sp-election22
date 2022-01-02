from PIL import Image
import pytesseract
from pdf2image import convert_from_path

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("first_page", type=int)
parser.add_argument("--num-pages", type=int, default=4)
args = parser.parse_args()

images = convert_from_path(
    '/home/felix/git/ocr_wahlzeitungsbeitraege22/Wahlzeitung_2022.pdf',
    dpi=300,
    thread_count=12,
    first_page=args.first_page,
    last_page=args.first_page + args.num_pages - 1
)

for idx, img in enumerate(images):
    print(f"~~~ PAGE {idx + args.first_page} ~~~")
    print(pytesseract.image_to_string(img, lang='deu'))
