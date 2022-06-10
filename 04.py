#!/usr/bin/python3
# -*- coding: utf-8 -*-

def get_line_pixels():
    """ Získání linie pixelů """
    pixels = []
    for x in range(0, 256, 4):
        pixels.append([x, x, 0])
    for x in range(255, 0, -4):
        pixels.append([x, x, 0])
    print(len(pixels))
    return pixels

def write_to_file():
    """ Vytvoření obrázku """
    line_of_pixels = get_line_pixels()
    with open('yellow.ppm', 'w') as file_to_write:
        file_to_write.write('P3' + '\n')
        file_to_write.write('128 256' + '\n')
        file_to_write.write('255' + '\n')
        for _ in range(256):
            for pixel in line_of_pixels:
                file_to_write.write(str(pixel[0]) + ' ' + str(pixel[1]) + ' ' + str(pixel[2]) + '\n')

def main():
    """ Hlavní funkce """
    write_to_file()

if __name__ == "__main__":
    main()
