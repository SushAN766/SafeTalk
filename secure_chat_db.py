# secure_chat_db.py

import os
import base64
import mysql.connector
from dotenv import load_dotenv
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Load environment variables
load_dotenv()

# MySQL Database Configuration
db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "database": os.getenv("DB_NAME"),
    "auth_plugin": os.getenv("DB_AUTH_PLUGIN")
}

# Secret AES key (16, 24, or 32 bytes)
SECRET_KEY = os.getenv("SECRET_KEY").encode()

# AES Encryption Function
def encrypt_message(message):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC)
    iv = cipher.iv
    encrypted = cipher.encrypt(pad(message.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted).decode()

# AES Decryption Function
def decrypt_message(encrypted_message):
    raw = base64.b64decode(encrypted_message)
    iv = raw[:AES.block_size]
    encrypted = raw[AES.block_size:]
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(encrypted), AES.block_size).decode()

# Database Connection
def connect_db():
    return mysql.connector.connect(**db_config)

print("✓ Connected to MySQL Database")
