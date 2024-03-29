from PIL import Image, ImageFilter
import os

files = os.listdir()
files.remove('venv')
files.remove('filtres.py')

def pinkify(path):
    obrazek = Image.open(path)
    sirka, vyska = obrazek.size

    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            # prumer = int((r+g+b)/3)
            obrazek.putpixel((x,y), (int(r**1.5),int(g**0.5),int(b**1.5/10)))
            y += 1
        x += 1
    # display(obrazek)
    obrazek.save("pink_"+path)
    obrazek.show()

def black_white(path):
    obrazek = Image.open(path)
    sirka, vyska = obrazek.size

    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/3)
            obrazek.putpixel((x,y), (prumer,prumer,prumer))
            y += 1
        x += 1
    # display(obrazek)
    obrazek.save("bw_"+path)
    obrazek.show()

def greenify(path):
    image = Image.open(path)
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            image.putpixel((x, y), (int(r*0.5), int(g*1.5), int(b*0.5)))
    image.save("green_"+path)
    image.show()

def blueify(path):
    image = Image.open(path)
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            image.putpixel((x, y), (int(r*0.5), int(g*0.5), int(b*1.5)))
    image.save("blue_"+path)
    image.show()

def redify(path):
    image = Image.open(path)
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            image.putpixel((x, y), (int(r*1.5), int(g*0.5), int(b*0.5)))
    image.save("red_"+path)
    image.show()

def blur_image(path):
    obrazek = Image.open(path)
    blurred = obrazek.filter(ImageFilter.GaussianBlur(5))
    blurred.save("blurred_" + path)
    blurred.show()

def color_shuffle(path):
    obrazek = Image.open(path)
    sirka, vyska = obrazek.size
    print('Dostupné styly shuffle: 1-GBR, 2-BRG, 3-RBG, 4-GRB, 5-BGR')
    choice = int(input("Zadej styl shuffle (1-5): "))-1
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            sh_styles = ((g,b,r),(b,r,g),(r,b,g),(g,r,b),(b,g,r))
            obrazek.putpixel((x,y), sh_styles[choice])
            y += 1
        x += 1
    obrazek.save("inverted_"+path)
    obrazek.show()
filters = {
    "pinkify": pinkify,
    "black-white": black_white,
    "greenify": greenify,
    "blueify": blueify,
    "redify": redify,
    "blur": blur_image,
    "shuffle": color_shuffle
}


print("\nVítej.")
print("Jaký soubor chceš editovat?")
# print("Dostupné soubory:",end=" ")
# print(*files,sep=", ")
for i in range(len(files)):
    print(f"{i+1}: {files[i]}")
image_file = files[int(input("Zadej číslo obrázku: "))-1]
print("Dostupné filtry:",end=" ")
print(*filters.keys(),sep=", ")
chosen_function = ""
while not chosen_function in filters.keys():
    chosen_function = input("Vyber filtr: ")

filters[chosen_function](image_file)


