from PIL import Image
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
    image.save("green_"+path)
    image.show()

filters = {
    "pinkify": pinkify,
    "black-white": black_white,
    "greenify": greenify,
    "blueify": blueify,
    "redify": redify
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
