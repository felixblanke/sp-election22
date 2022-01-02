# Quantitative analysis of the statements of the candidates for the election of the 44th student's parliament of Bonn

We want to analyze the statements of the seven lists candidating for the [election of the 44th student's parliament](https://wahlen.uni-bonn.de) of Bonn.
These statements were published in the [election magazine](https://wahlen.uni-bonn.de/content/dokumente/2022/Wahlzeitung_2022.pdf) and each span four pages.

### Preprocessing

First, we have to extract the statements from the published pdf file.
For this we need to resort to optical character recognition (OCR) since some statements are included as page-spanning images. For the OCR, we use the [python wrapper of `tesseract`](https://pypi.org/project/pytesseract/). For the extraction of pdf pages as images we use [`pdf2image`](https://pypi.org/project/pdf2image/).

The ocr script can be found in `ocr.py`.
```
usage: OCR recognition of pdf pages [-h] [--path PATH] [--num-pages NUM_PAGES] [--lang LANG] first_page

Transforms pdf pages to Pillow Images using pdf2image and then uses tesseract for OCR. The recognized text is printed to stdout.

positional arguments:
  first_page            Number of the first page to consider

optional arguments:
  -h, --help            show this help message and exit
  --path PATH           Path of the pdf file (default: Wahlzeitung_2022.pdf)
  --num-pages NUM_PAGES
                        Number of pages to consider, starting from first_page (default: 4)
  --lang LANG           three letter language code of the text to recognize (default: deu)
```

It can be invoked as
```bash
$ python ocr.py 34 > lp.log
```

The resulting text needs some (manual) processing, mostly due to misrecognized two-column layouts. You can finde our processed texts in the `data` folder. We decided to remove the names of individual candidates and their subjects (which are included in some statements).

### Analysis
*to be added*


## Transparency note

The author is himself a candidate for the [Liste Poppelsdorf](https://liste-poppelsdorf.de).
