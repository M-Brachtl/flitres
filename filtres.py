from PIL import Image

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
    obrazek.show()

filters = {
    "pinkify": pinkify,
    "black-white": black_white
}


print("\nVítej.")
print("Jaký soubor chceš editovat?")
image_file = input("./")
chosen_function = ""
while not chosen_function in filters.keys():
    chosen_function = input("Vyber filtr: ")

filters[chosen_function](image_file)



