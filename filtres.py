from PIL import Image

print("Vítej.")
print("Jaký soubor chceš editovat?")
image_file = input("-> ")
chosen_function = input("Vyber filtr: ")

def pinkify(obrazek):
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
    display(obrazek)

def black_white(obrazek):
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
    display(obrazek)

