from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from PIL import Image
import os
#function to encrypt the image
def encrypt_image(image_path,key,iv):
    #open to image and convert into byte array
    with open (image_path,'rb') as image_file:
        image_bytes=image_file.read()
        #pad the image bytes to be multiple block size
        padder=padding.PKCS7(128).padder()
        padder_data=padder.update(image_bytes)+padder.finalize()
        #create cipher object and encrypt the data
        cipher=Cipher(algorithms.AES(key),modes.CBC(iv),backend=default_backend())
        encryptor=cipher.encryptor
        encrypted_data = encryptor.update(padder_data)+encryptor.finalize()
        with('encrypted_image.enc','wb')as enc_file:
            enc_file.write(encrypted_data)
            #function to decrypt the image
            def decrypt_image(encrypted_path,key,iv,output_path):
                with open(encrypted_path,'rb')as enc_file:
                    encrypted_data=enc_file.read()
                    cipher=Cipher(algorithms.AES(key),modes.CBC(iv),backend=default_backend())
                    decryptor=cipher.decryptor()
                    decrypted_padded_data=decryptor.update(encrypted_data)+decryptor.finalize()
                    unpadder=padding.PKCS7(128).unpadder()
                    decrypted_data=unpadder.update(decrypted_padded_data)+unpadder.finalize()
                    with open (output_path,'wb')as image_file:
                        image_file.write(decrypted_data)
            key=os.urandom(32)
            iv=os.urandom(16)
            encrypt_image('C:\\Users\\LENOVO\\OneDrive\\Desktop\\dhoni1.jpeg',key,iv)
            decrypt_image('encrypted_image.enc',key,iv,'decrypted_image.jpeg')




