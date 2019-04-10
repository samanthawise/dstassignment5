#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:06:16 2019

@author: xihajun
"""

from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"A really secret message. Not for prying eyes.")
test = f.decrypt(token)


def Encrypt(filename):

    real_filename = '../books/' + filename
    output_filename = '../data/encoded_books/' + filename
    output_key = '../data/key/' + filename
    data = ''
    # open file wiht binary form
    with open(real_filename, 'rb') as file:
        data = file.read()

        
    with open(output_filename, 'wb') as out_file:
        # recipient key - public key
        key = Fernet.generate_key()
        f = Fernet(key)
        ciphertext = f.encrypt(data)
        out_file.write(ciphertext)
        
        with open(output_key, 'wb') as mykey:
            mykey.write(key)
        
filename = []
for i in range(3001,3030):
    filename.append("%04d.txt"%i)

list(map(Encrypt,filename))

def Decrypt(filename):
    decrypt_filename = '../data/encoded_books/' + filename
    output_filename = '../data/decoded_books/' + filename
    output_key = '../data/key/' + filename
    key = ''
    # open file wiht binary form
    with open(output_key, 'rb') as file:
        key = file.read()
    
    with open(decrypt_filename, 'rb') as file:
        token = file.read()
    with open(output_filename, 'wb') as out_file:
        f = Fernet(key)
        
        out_file.write(f.decrypt(token))
        
list(map(Decrypt,filename))
