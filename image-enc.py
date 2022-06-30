import cv2
import math
import numpy as np


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

def imageDecryption(EncryptionImg, j0, g0, x0, DecryptionImg):
    x = EncryptionImg.shape[0]
    y = EncryptionImg.shape[1]
    c = EncryptionImg.shape[2]
    g0 = int2bin16(g0)
    for s in range(x):
        for n in range(y):
            for z in range(c):
                cc = int2bin8(img[s][n][z])
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


if __name__ == "__main__":
    img = cv2.imread(r"C:/Users/Zeus/Downloads/CyberSecProject/ttieOutput2.png", 1)

    EncryptionImg = np.zeros(img.shape, np.uint8)
    imageEncryption(img, 10, 30, 0.123345, EncryptionImg)

    # Saving the Encrypted Image
    cv2.imwrite(r"C:/Users/Zeus/Downloads/CyberSecProject/ttieOutput2Enc.png", EncryptionImg)

    img = cv2.imread(r"C:/Users/Zeus/Downloads/CyberSecProject/ttieOutput2Enc.png", 1)
    DecryptionImg = np.zeros(img.shape, np.uint8)
    imageDecryption(img, 10, 30, 0.123345, DecryptionImg)

    # Saving the Decrypted Image
    cv2.imwrite(r"C:/Users/Zeus/Downloads/CyberSecProject/ttieOutput2Dec.png", DecryptionImg)

    # cv2.waitKey(0)