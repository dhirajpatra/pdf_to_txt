# importing required modules
# import PyPDF2
import argparse
from pdfminer.high_level import extract_text
from os import system, name


def main(pdf_file):
    text = extract_text(pdf_file)
    text_file = open('output.txt', 'w+')
    text_file.write(text)
    text_file.close()

# def main(pdf_file):
#     # creating a pdf file object
#     pdf_file_obj = open(pdf_file, 'rb')
#
#     # creating a pdf reader object
#     pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
#
#     # printing number of pages in pdf file
#     print(pdf_reader.numPages)
#
#     # creating a page object
#     page_obj = pdf_reader.getPage(0)
#
#     # extracting text from page
#     print(page_obj.extractText())
#
#     # closing the pdf file object
#     pdf_file_obj.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    system('clear')
    # give the pdf path --pdffile argument
    parser = argparse.ArgumentParser(description='Read a PDF and convert to text file')
    parser.add_argument('--pdffile', metavar='path', required=True,
                        help='the path of the pdf file')
    args = parser.parse_args()
    pdf_file = args.pdffile
    # pdf_file = '/Users/dhirajpatra/Desktop/books/My_Life_and_Work.pdf'
    # pdf_file = '/Users/dhirajpatra/Desktop/books/isaacson2011stevejobs.pdf'
    main(pdf_file)

