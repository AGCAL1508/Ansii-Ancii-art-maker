from PIL import Image, ImageEnhance
from colors_ansi_to_rgb_data import colors
from colors_ansi_to_rgb_data import colors_list
img = Image.open("Image.webp", "r")
img_enhance = ImageEnhance.Contrast(img)
img = img_enhance.enhance(4)
basewidth = 130
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img_data = img.getdata()
img_dimensions = img.size
img_width = img_dimensions[0]
img_height = img_dimensions[1]
img_data = [list(img_data)[b:b+img_width] for b in range(0,len(img_data),img_width)]
ascii_art = False
char = '.,:*[%#'
text_counter = 0
for pixely in img_data:
    for pixels in pixely:
        pixel_hex_int = int("0x%02X%02X%02X"%(pixels[0],pixels[1],pixels[2]),16)
        colors.append(pixel_hex_int)
        colors.sort()
        pixel_index = colors.index(pixel_hex_int)
        # print(pixel_index)
        colors.pop(pixel_index)
        if ascii_art:
            print(f'{colors_list[pixel_index]}{char[int((sum(pixels)/3)//36)-3]}\u001b[0m',end=" ")
        else:
            print(f'{colors_list[pixel_index]}#\u001b[0m',end=" ")
    print()
