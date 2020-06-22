from PIL import Image
import pytesseract

im = Image.open("test_img/parag_01.jpg")
text = pytesseract.image_to_string(im, lang='pol')
print(text)

