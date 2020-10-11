## Small PDF converter to text

I have found that it almost impossible to convert a big PDF which is strictly fixed width pdf. If I convert into
 .mobi format for my kindle papaerwhite, I can't read. 
 
That why I have just used the pdfminer and created a small command prompt srcipt to convert a pdf to a text file.

#### How to install

- `$ pip install pdfminer.six`
- `$ python main.py --pdffile <file-path>/<pdf-file-name>.pdf`

After convert and create txt file [it can takes few minutes depends on the size and complexity of pdf]. Move the
 output.txt to your intended name eg. `mv output.txt henry_ford.txt`
 
Then you can use calibre for converting txt to .mobi for your kindly. And then you can change the size and super to
 read in any size :)