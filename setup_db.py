# setup_db.py
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_AUTH = os.getenv("DB_AUTH_PLUGIN", "mysql_native_password")

conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASS,
    auth_plugin=DB_AUTH,
)

cursor = conn.cursor()

cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
cursor.execute(f"USE {DB_NAME}")

# Users table for login system
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    password_hash VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Messages table
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender VARCHAR(255),
    receiver VARCHAR(255),
    encrypted_message TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Index for faster inbox lookups
cursor.execute("""
SHOW INDEX FROM messages WHERE Key_name = 'idx_receiver'
""")
if not cursor.fetchall():
    cursor.execute("CREATE INDEX idx_receiver ON messages(receiver)")

conn.commit()
cursor.close()
conn.close()

print("✓ Database, users table, and messages table created/verified.")
