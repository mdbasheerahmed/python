# pip install python_barcode
# pip install pillow
import barcode
import IPython
from barcode.writer import ImageWriter
from IPython.display import Image, display

barcode_format = barcode.get_barcode_class('ean13')
print("Python working")

barcode_number = '1234567895840'

barcode_image = barcode_format(barcode_number, writer=ImageWriter())

barcode_filename = 'barcode_image'
barcode_image.save(barcode_filename)

display(Image(filename=f'{barcode_filename}.png'))