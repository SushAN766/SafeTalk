import socket
import threading
import sys
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 5555))


def safe_print(msg):
    """Print incoming messages without breaking input prompt."""
    sys.stdout.write("\r" + " " * 80 + "\r")  # Clear line
    print(msg)
    sys.stdout.write("Receiver: ")
    sys.stdout.flush()


def receive_messages(sock):
    try:
        while True:
            data = sock.recv(4096)
            if not data:
                safe_print("Server closed connection.")
                break

            msg = data.decode("utf-8")
            safe_print(msg)

    except Exception:
        safe_print("Disconnected from server.")
    finally:
        sock.close()


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    username = input("Enter your username: ").strip()
    sock.send(username.encode("utf-8"))

    threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()

    try:
        while True:
            receiver = input("Receiver: ").strip()
            message = input("Message: ").strip()

            if not receiver or not message:
                print("Both receiver and message required.\n")
                continue

            full = f"{username}:{receiver}:{message}"
            sock.send(full.encode("utf-8"))

    except KeyboardInterrupt:
        print("\nExiting client.")
    finally:
        sock.close()


if __name__ == "__main__":
    main()
