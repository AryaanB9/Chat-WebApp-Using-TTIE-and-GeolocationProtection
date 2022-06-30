# For FLASK and Socket Programming
from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room

# FOR AES
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# FOR RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from base64 import b64decode

# FOR TTIE
from PIL import Image
import PIL
import random

# FOR IMAGE ENCRYPTION
import cv2
import math
import numpy as np

# AES Decrypt
def decryptAES(enc, key):
    enc = base64.b64decode(enc)
    # cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    return unpad(cipher.decrypt(enc), 16)

# RSA Decrypt
def decryptRSA(encrRSA):
    key = RSA.importKey(open('privatekey.pem').read())
    cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)
    decrypted_message = cipher.decrypt(b64decode(encrRSA))
    str1 = decrypted_message.decode('utf-8')
    return str1

# ===========================================
# Diffie Hellman Algorithm
# =========================================
# A prime number P is taken
P = 137
# A primitive root for P, G is taken
G = 29
# User 1 will choose the private key a
a = 5
# User 2 will choose the private key b
b = 7
# Generated Secret Key for User 1
ka = 0

# skey = secret key, pkey = private key, prime = prime number
def dhalgo(skey, pkey, prime, check):
    key1 = int(pow(skey, pkey, prime)) # X^a mod prime
    if check == 0:
        return key1
    elif check == 1:
        global ka
        # Generated Secret Key for User 1
        ka = int(pow(key1, a, P))
        return key1

# Diffie Hellman Key Exchange

# Shared Secret Key of User 1
x = dhalgo(G, a, P, 0)

# Shared Secret Key of User 2
# y = dhalgo(G, b, P, 0)
y = -1
# =========================================

# =========================================
# TEXT TO IMAGE ENCRYPTION ALGORITHM
# =========================================
def ttieEncrypt(text, len, private_key):
    ttieImage = Image.new('RGB', (len, len))

    # For First Plane Of Encryption
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
    ttieImage.save('./SavedImagesLogs/ttieOutput.png')

    # For Second Plane i.e. Correction Plane
    for i in range(int(len/2)):
        # pixel_value = ord(text[i])
        for j in range(len):
            pixels_value = ttieImage.getpixel((i, j))
            ttieImage.putpixel((i, j), (pixels_value[0]+private_key, pixels_value[1]+private_key, pixels_value[2]+private_key))

    # Saving the image after two layers of Text to Image Encryption
    ttieImage.save('./SavedImagesLogs/ttieOutput2.png')
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

# =========================================
# IMAGE ENCRYPTION ALGORITHM
# =========================================
def int2bin8(x):
    result = ""
    for i in range(8):
        y=x&(1)
        result+=str(y)
        x=x>>1
    return result[::-1]

def int2bin16(x):
    result=""
    for i in range(16):
        y=x&(1)
        result+=str(y)
        x=x>>1
    return result

def imageEncryption(img, j0, g0, x0, EncryptionImg):
    x = img.shape[0]
    y = img.shape[1]
    c = img.shape[2]
    g0 = int2bin16(g0)
    for s in range(x):
        for n in range(y):
            for z in range(c):
                m = int2bin8(img[s][n][z])                   # Pixel value to octet binary
                ans=""
                for i in range(8):
                    ri=int(g0[-1])                           # Take the last digit of the manual cipher machine
                    qi=int(m[i])^ri                          # XOR with pixel value qi
                    xi = 1 - math.sqrt(abs(2 * x0 - 1))      # f1(x) chaotic iteration
                    if qi==0:                                # If qi=0, use x0i+x1i=1;
                        xi=1-xi;
                    x0=xi                                    # xi iteration
                    t=int(g0[0])^int(g0[12])^int(g0[15])     # Primitive polynomial x^15+x^3+1
                    g0=str(t)+g0[0:-1]                       # gi iteration
                    ci=math.floor(xi*(2**j0))%2              # Nonlinear transformation operator
                    ans+=str(ci)
                re=int(ans,2)
                EncryptionImg[s][n][z]=re                    # Write new image

img = cv2.imread(r"./SavedImagesLogs/ttieOutput2.png", 1)

def imageDecryption(EncryptionImg, j0, g0, x0, DecryptionImg):
    x = EncryptionImg.shape[0]
    y = EncryptionImg.shape[1]
    c = EncryptionImg.shape[2]
    g0 = int2bin16(g0)
    for s in range(x):
        for n in range(y):
            for z in range(c):
                cc = int2bin8(EncryptionImg[s][n][z])
                ans = ""
                for i in range(8):
                    xi = 1 - math.sqrt(abs(2 * x0 - 1))
                    x0 = xi
                    ssi = math.floor(xi * (2 ** j0)) % 2
                    qi=1-(ssi^int(cc[i]))
                    ri = int(g0[-1])
                    mi=ri^qi
                    t = int(g0[0]) ^ int(g0[12]) ^ int(g0[15])
                    g0 = str(t) + g0[0:-1]
                    ans += str(mi)
                re = int(ans, 2)
                DecryptionImg[s][n][z] = re

# ==================================================================================

# =========================================
# FLASK & SOCKETIO
# =========================================

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/chat')
def chat():
    username = request.args.get('username')
    room = request.args.get('room')
    return render_template('chat.html', username=username, room=room)


@socketio.on('send_message')
def handle_send_message_event(data):
    print("{} has sent message to the room {}! Message : {}".format(data['username'], data['room'], data['message']))
    encAES = data['encAES']
    encRSA = data['encRSA']

    # =========================================
    # DIFFIE HELLMAN KEY EXCHANGE ALGORITHM
    # Shared Secret Key of User 2
    y = dhalgo(G, b, P, 1)

    # Generated Secret Key for User 2
    kb = dhalgo(x, b, P, 0)

    # Checking the Keys Generated
    print(x, y, ka, kb)


    # =========================================
    # TTIE : encRSA to image

    no_pixels = len(encRSA)
    # ttie_image = PIL.Image.open("ttieOutput.png")
    # ttie_image_rgb = ttie_image.convert("RGB")
    ttieEncryptedImage = ttieEncrypt(encRSA, no_pixels, ka)


    # =========================================
    # IMAGE ENCRYPTION
    img = cv2.imread(r"./SavedImagesLogs/ttieOutput2.png", 1)

    EncryptionImg = np.zeros(img.shape, np.uint8)
    imageEncryption(img, 10, 30, 0.123345, EncryptionImg)

    # Saving the Encrypted Image
    cv2.imwrite(r"./SavedImagesLogs/ttieOutput2Enc.png", EncryptionImg)

    # =========================================
    # IMAGE DECRYPTION
    img = cv2.imread(r"./SavedImagesLogs/ttieOutput2Enc.png", 1)
    DecryptionImg = np.zeros(img.shape, np.uint8)
    imageDecryption(img, 10, 30, 0.123345, DecryptionImg)

    # Saving the Decrypted Image
    cv2.imwrite(r"./SavedImagesLogs/ttieOutput2Dec.png", DecryptionImg)

    # =========================================
    # TTIE DECRYPTION
    ttieDecryptedText = ttieDecrypt(ttieEncryptedImage, no_pixels, kb)
    print("RSA Key Obtained after TTIE Decryption")
    print(ttieDecryptedText)

    # =========================================
    # RSA DECRYPTION TO GET AES KEY
    str2 = str(encRSA)
    decryptedRSA = decryptRSA(str2)

    # =========================================
    # AES DECRYPTION TO GET MESSAGE
    key = decryptedRSA
    decryptedAES = decryptAES(encAES, key)
    data['message'] = decryptedAES.decode("utf-8", "ignore")
    print('Message: ', decryptedAES.decode("utf-8", "ignore"))


    # data['created_at'] = datetime.now().strftime("%d %b, %H:%M")
    # save_message(data['room'], data['message'], data['username'])
    socketio.emit('receive_message', data, room=data['room'])
    # socketio.emit('enc_message', data, room=data['room'])


@socketio.on('join_room')
def handle_join_room_event(data):
    app.logger.info("{} has joined the room {}".format(data['username'], data['room']))
    join_room(data['room'])
    socketio.emit('join_room_announcement', data, room=data['room'])


if __name__ == '__main__':
    socketio.run(app)