#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet
files = []
for file in os.listdir():
    if file == "run.py":
         exit(-1)
    if file == "decrypt.py" or file == "keyfile" or file == ".gitattributes":
        continue
    if os.path.isfile(file):
        files.append(file)
with open("keyfile", "rb") as keycontent:
    key = keycontent.read()
for file in files:
        with open(file, "rb") as filecontent:
            enc_content = filecontent.read()
        dec_content = Fernet(key).decrypt(enc_content)
        with open(file, "wb") as filecontent:
            filecontent.write(dec_content)
with open("keyfile", "w") as keycontent:
    keycontent.write("")
os.remove("keyfile")
with open("decrypt.py", "rb") as filecontent:
     filecontent.write("")
os.remove("decrypt.py")