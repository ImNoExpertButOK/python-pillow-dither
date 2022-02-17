from PIL import Image

img = Image.open("base_image.jpeg").convert("L")
print("Total pixels:", img.height * img.width)

limit = 128

for v_pixel in range(img.height):
    for h_pixel in range(img.width):

        old_value = img.getpixel((h_pixel, v_pixel))
        new_value = 0 if old_value < limit else 255
        img.putpixel(xy = (h_pixel, v_pixel), value = new_value)
        error = old_value - new_value

        try:
            img.putpixel(xy = (h_pixel + 1, v_pixel), value = int(error * 7 / 16 + (img.getpixel((h_pixel + 1, v_pixel)))))
            img.putpixel(xy = (h_pixel + 1, v_pixel + 1), value = int(error * 1 / 16 + (img.getpixel((h_pixel + 1, v_pixel + 1)))))
            img.putpixel(xy = (h_pixel, v_pixel + 1), value = int(error * 5 / 16 + (img.getpixel((h_pixel, v_pixel + 1)))))
            img.putpixel(xy = (h_pixel - 1, v_pixel + 1), value = int(error * 3 / 16 + (img.getpixel((h_pixel - 1, v_pixel + 1)))))
        except IndexError:
            pass

img.save("output.png")
