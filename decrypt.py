#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet
os.remove("run.py")
files = []
for file in os.listdir():
    if file == "decrypt.py" or file == "keyfile" or file == ".gitattributes":
        continue
    if os.path.isfile(file):
        files.append(file)
with open("keyfile", "rb") as keycontent:
    key = keycontent.read()
with open("keyfile", "w") as keycontent:
    keycontent.write("")
for file in files:
        with open(file, "rb") as filecontent:
            enc_content = filecontent.read()
        dec_content = Fernet(key).decrypt(enc_content)
        with open(file, "wb") as filecontent:
            filecontent.write(dec_content)
with open("decrypt.py", "rb") as filecontent:
     content = filecontent.read()
enc_content = Fernet(key).encrypt(content)
key = ""
os.remove("keyfile")
with open("decrypt.py", "wb") as filecontent:
     filecontent.write(enc_content)
os.remove("decrypt.py")