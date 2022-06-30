# #==============================================================
# ===== AES ===== ===== AES ===== ===== AES ===== ===== AES =====
# #==============================================================

# import base64
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad, unpad
#
# #AES ECB mode without IV
#
# data = 'Hey I am Aryaan'
# key = 'AAAAAAAAAAAAAAAA' #Must Be 16 char for AES128
#
# def encrypt(raw):
#         raw = pad(raw.encode(),16)
#         # cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
#         cipher = AES.new(key.encode(), AES.MODE_ECB)
#         return base64.b64encode(cipher.encrypt(raw))
#
# def decrypt(enc):
#         enc = base64.b64decode(enc)
#         # cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
#         cipher = AES.new(key.encode(), AES.MODE_ECB)
#         return unpad(cipher.decrypt(enc), 16)
#
# # encrypted = encrypt(data)
# # # print('Encrypted ECB Base64 : ', encrypted.decode("utf-8", "ignore"))
# # print('Encrypted ECB Base64 : ', encrypted.decode())
#
# encrypted = 'kHIFwvWXCyb65cs+UxrbUA=='
# decrypted = decrypt(encrypted)
# print('Data : ', decrypted.decode("utf-8", "ignore"))

# #=================================================================
# #=================================================================



# #==============================================================
# ===== RSA ===== ===== RSA ===== ===== RSA ===== ===== RSA =====
# #==============================================================
# import base64
# from Crypto.PublicKey import RSA
# # 1024 means the keysize will be 1024
# key_pair = RSA.generate(1024)
# private_key = open("privatekey.pem", "wb")
# # private_key.write(key_pair.exportKey())
# # key1 = key_pair.encode('utf-8')
# # b64 = base64.b64encode(key_pair)
#
# private_key.write(key_pair.exportKey())
#
# private_key.close()
# public_key = open("public_key.pem", "wb")
# public_key.write(key_pair.publickey().exportKey())
# public_key.close()

#     Public key = This key will be used for encryption and does not have the ability to decrypt messages.
#     Private key = This key will be used for decryption.
#     MAN IN THE MIDDLE ATTACKS CAN BE PREVENTED
# #=================================================================

# from Crypto.Cipher import PKCS1_OAEP
# from Crypto.PublicKey import RSA
# from Crypto.Hash import SHA256
# from base64 import b64decode
# import base64

# privkey =  '-----BEGIN RSA PRIVATE KEY----- MIICXQIBAAKBgQDTSE3PXbkazI+zJtI6HudRsh5Dr1HAnebLlH34A6cuGjmJzo+HQxlZcdoyGl9QqqHDJvzJ0Z436kcRp4tzinvaMPravQkcLcefo+I+ZTNIEG28mT2y6qf9YqlsIiBfPUysenMEV+8tqQrAZZ70T2bDtflG20Cg8fnVi7H5TrHQ3wIDAQABAoGAUPZohrmB+LCBsmOCdK4p8ybfrQ0uNTLs4X8+BD+WHTcEbHfgjTMbsChONhvgAX/Za/hxLv8p84BNiojbCcP78C7LDN554CspHf0zmWIhMFMgOk71lJb4QcK/LyBwnqAM+qAObNSA8EOg9WOWhA8dCefT487/R2Laz8ODqmnu4DkCQQDl/aaPoNoi7Z51hAAZryhYUyfkPQ1A9mP30ebx+F8NheKW/S3aetQuuUqosLDUz+xvPYhimTCofwAFcTSwNFJXAkEA6y0JREJTXxBoL3fZXqYkDFwHxEoFYaLKYgJz0RZMdZuHn7Za5aL8+BdVy6bDafEfFQ0fzAhfNMJSSYJkDt4wuQJBALuvlX9ceudKFqg8AoDzSe9aXRGLKQe8irQwXVFVqOw2OEWTcxn6ZrGCkIS9PHFPBNl605PzA5xdl7zZN3AcIp0CQQDq+oLJyyOWVsRiuXNdWM+n8cRo4jTiS0/AAgdKoOcgk5g9gmzsCaCNGnPFGgkir6OI2yYsLSlDg+3IORpUqLkxAkBM6Ot3IJkBzvwoTNNQ3gJiojZneT0uXHFwGDox7teuz0apKr7DcRmkJjMC0MUdGFWAxEhjZyZ9ZC3okelRC7Eu -----END RSA PRIVATE KEY-----'
# privkey2 = '-----BEGIN RSA PRIVATE KEY----- \\nMIICXQIBAAKBgQDTSE3PXbkazI+zJtI6HudRsh5Dr1HAnebLlH34A6cuGjmJzo+H\\nQxlZcdoyGl9QqqHDJvzJ0Z436kcRp4tzinvaMPravQkcLcefo+I+ZTNIEG28mT2y\\n6qf9YqlsIiBfPUysenMEV+8tqQrAZZ70T2bDtflG20Cg8fnVi7H5TrHQ3wIDAQAB\\nAoGAUPZohrmB+LCBsmOCdK4p8ybfrQ0uNTLs4X8+BD+WHTcEbHfgjTMbsChONhvg\\nAX/Za/hxLv8p84BNiojbCcP78C7LDN554CspHf0zmWIhMFMgOk71lJb4QcK/LyBw\\nnqAM+qAObNSA8EOg9WOWhA8dCefT487/R2Laz8ODqmnu4DkCQQDl/aaPoNoi7Z51\\nhAAZryhYUyfkPQ1A9mP30ebx+F8NheKW/S3aetQuuUqosLDUz+xvPYhimTCofwAF\\ncTSwNFJXAkEA6y0JREJTXxBoL3fZXqYkDFwHxEoFYaLKYgJz0RZMdZuHn7Za5aL8\\n+BdVy6bDafEfFQ0fzAhfNMJSSYJkDt4wuQJBALuvlX9ceudKFqg8AoDzSe9aXRGL\\nKQe8irQwXVFVqOw2OEWTcxn6ZrGCkIS9PHFPBNl605PzA5xdl7zZN3AcIp0CQQDq\\n+oLJyyOWVsRiuXNdWM+n8cRo4jTiS0/AAgdKoOcgk5g9gmzsCaCNGnPFGgkir6OI\\n2yYsLSlDg+3IORpUqLkxAkBM6Ot3IJkBzvwoTNNQ3gJiojZneT0uXHFwGDox7teu\\nz0apKr7DcRmkJjMC0MUdGFWAxEhjZyZ9ZC3okelRC7Eu\\n-----END RSA PRIVATE KEY-----'
# key = RSA.importKey(privkey2)


key = RSA.importKey(open('privatekey.pem').read())
cipher = PKCS1_OAEP.new(key, hashAlgo=SHA256)
decrypted_message = cipher.decrypt(b64decode('k1bbJRP1qW/249N7xpifdhtt6g9KutvFcFad64vlIVFT6dwm1fo/Gf6YDaxl7NWYllsRVc2iwrrqYZSiJVz+kPTF7w2lYO6jla/GCMmvN2xQ7X1LqwQoPW0buwqqnSX9/Qk1INhOxGrD7apMtk0Kn4awidvzJuArmfrJPSle+AY='))

print(decrypted_message)
str1 = decrypted_message.decode('utf-8')
print(str1)


# cipher = PKCS1_OAEP.new(key)
# message = cipher.decrypt(ciphertext)


# #=================================================================
# #=================================================================