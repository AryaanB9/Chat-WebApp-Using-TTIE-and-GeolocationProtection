from PIL import Image
import PIL
import random

def ttieEncrypt(text, len, private_key):
    ttieImage = Image.new('RGB', (len, len))

    # For First Plane
    for i in range(len):
        pixel_value = ord(text[i])
        if i % 3 == 0:
            for j in range(len):
                n2 = random.randint(0, 127)
                n3 = random.randint(0, 127)
                ttieImage.putpixel((i, j), (pixel_value, n2, n3))
        elif i % 3 == 1:
            for j in range(len):
                n1 = random.randint(0, 127)
                n3 = random.randint(0, 127)
                ttieImage.putpixel((i, j), (n1, pixel_value, n3))
        else:
            for j in range(len):
                n1 = random.randint(0, 127)
                n2 = random.randint(0, 127)
                ttieImage.putpixel((i, j), (n1, n2, pixel_value))
    ttieImage.save('C:/Users/Zeus/Downloads/CyberSecProject/ttieOutput.png')

    # For Second Plane i.e. Correction Plane
    for i in range(int(len/2)):
        # pixel_value = ord(text[i])
        for j in range(len):
            pixels_value = ttieImage.getpixel((i, j))
            ttieImage.putpixel((i, j), (pixels_value[0]+private_key, pixels_value[1]+private_key, pixels_value[2]+private_key))

    # Saving the image after two layers of Text to Image Encryption
    ttieImage.save('C:/Users/Zeus/Downloads/CyberSecProject/ttieOutput2.png')
    return ttieImage


def ttieDecrypt(ttieImage, len1, private_key):
    ttieText = ''
    ttieImageRGB = ttieImage.convert('RGB')
    for i in range(len1):
        if i<int(len1/2):
            if i % 3 == 0:
                for j in range(len1):
                    pixels_value = ttieImageRGB.getpixel((i, j))
                    value = pixels_value[0] - private_key;
                    # value = pixels_value[0];
                    ttieText = ttieText + chr(value)
                    break;
            if i % 3 == 1:
                for j in range(len1):
                    pixels_value = ttieImageRGB.getpixel((i, j))
                    value = pixels_value[1] - private_key;
                    # value = pixels_value[1];
                    ttieText = ttieText + chr(value)
                    break;
            else:
                for j in range(len1):
                    pixels_value = ttieImageRGB.getpixel((i, j))
                    value = pixels_value[2] - private_key;
                    # value = pixels_value[2];
                    ttieText = ttieText + chr(value)
                    break;
        else:
            if i % 3 == 0:
                for j in range(len1):
                    pixels_value = ttieImageRGB.getpixel((i, j))
                    # value = pixels_value[0] - private_key;
                    value = pixels_value[0];
                    ttieText = ttieText+chr(value)
                    break;
            if i % 3 == 1:
                for j in range(len1):
                    pixels_value = ttieImageRGB.getpixel((i, j))
                    # value = pixels_value[1] - private_key;
                    value = pixels_value[1];
                    ttieText = ttieText+chr(value)
                    break;
            else:
                for j in range(len1):
                    pixels_value = ttieImageRGB.getpixel((i, j))
                    # value = pixels_value[2] - private_key;
                    value = pixels_value[2];
                    ttieText = ttieText+chr(value)
                    break;

    # PERFORMING TEXT CORRECTION TO THE OUTPUT
    textCorr = ttieText[0]
    count = 0
    try :
        for i in range(2, len1*2):
            count = count + 1
            if count == 4:
                count = 0
                continue
            else:
                textCorr = textCorr + ttieText[i]
    except:
        return textCorr

plaintext = "0ricmkbwzmuxA/GiwIIqZiOoNk5DzW56CUEubxs1FI6BUUlo1pcZHzB35cxzpjC4PLV9W3bLG1y24YHkAzQhuZY8aSiZFfE7gyoNr0Q3CoUfGXI2xABcQ1yLRUWsxC/ByswsnPE1D7ynZV1fDgWgINKQraPULy8vyLKJCKH8nZ8="
# plaintext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
no_pixels = len(plaintext)

ttie_image = PIL.Image.open("ttieOutput.png")
ttie_image_rgb = ttie_image.convert("RGB")

# wallpaper = ttieEncrypt(plaintext, no_pixels, 114)
wallpaper = PIL.Image.open("C:/Users/Zeus/Downloads/CyberSecProject/ttieOutput2Dec.png")
# wallpaper1 = ttie_image.convert("RGB")
ttieDecryptedText = ttieDecrypt(wallpaper1, no_pixels, 114)
print(ttieDecryptedText)

# rgb_pixel_value = red_image_rgb.getpixel((10, 15))
# rgb_pixel_value = wallpaper.getpixel((10, 15))

# print(rgb_pixel_value)
# print(rgb_pixel_value[0])
wallpaper.show()