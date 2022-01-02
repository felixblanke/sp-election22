from PIL import Image
import pytesseract
from pdf2image import convert_from_path

import argparse

parser = argparse.ArgumentParser(
    "OCR recognition of pdf pages",
    description="Transforms pdf pages to Pillow Images using pdf2image and then uses\
        tesseract for OCR. The recognized text is printed to stdout."
)
parser.add_argument("first_page", type=int, help="Number of the first page to consider")
parser.add_argument(
    "--path",
    type=str,
    default="Wahlzeitung_2022.pdf",
    help="Path of the pdf file (default: Wahlzeitung_2022.pdf)"
)
parser.add_argument(
    "--num-pages",
    type=int,
    default=4,
    help="Number of pages to consider, starting from first_page (default: 4)"
)
parser.add_argument(
    "--lang",
    type=str,
    default="deu",
    help="three letter language code of the text to recognize (default: deu)"
)
args = parser.parse_args()

images = convert_from_path(
    args.path,
    dpi=300,
    thread_count=12,
    first_page=args.first_page,
    last_page=args.first_page + args.num_pages - 1
)

for idx, img in enumerate(images):
    print(f"~~~ PAGE {idx + args.first_page} ~~~")
    print(pytesseract.image_to_string(img, lang=args.lang))
