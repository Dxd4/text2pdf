from fpdf import FPDF
import random
from PIL import Image

alphabet_img = "alphabet.jpg" # 1624x1919
pdf = FPDF()
word = input("text: ")
letter_number = 0
string_number = 0
pdf_string = 0
alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

def image_out(pdf, alphabet, alph_letter, word_letter, string_number, pdf_string):
    # alphabet coordinates
    letter_style = random.randint(0,2)
    
    x0, y0 = 7+135*(alph_letter*3-string_number*4*3+letter_style), 0+147*(string_number)
    x, y = 142+135*(alph_letter*3-string_number*4*3+letter_style), 147+147*(string_number)
    angle = random.randint(-4,4)
    # pdf page coordinates
    cropped_img = img.crop((x0, y0, x, y))

        
    img_x0, img_y0 = 0+10*(word_letter-30*pdf_string), 0+10*(pdf_string)
    
    pdf.image(cropped_img.rotate(angle,fillcolor=(255,255,255)), img_x0, img_y0, 10, 10)

with Image.open(alphabet_img) as img:
    pdf.add_page("L")

    for word_letter in range(len(word)):
        string_number=0
        for alph_letter in range(52):
            if alph_letter%4==0 and not alph_letter==0:
                string_number+=1
            if word[word_letter] == alphabet[(alph_letter)]:
                if (word_letter-30*pdf_string)>29:
                    pdf_string+=1
                if pdf_string>20:
                    continue
                image_out(pdf, alphabet, alph_letter, word_letter, string_number, pdf_string)
    
    pdf.output("yourfile.pdf")
