# store_retrieve.py
from secure_chat_db import connect_db, decrypt_message

def get_messages_for_receiver(receiver, limit=10, offset=0):
    db = connect_db()
    cur = db.cursor()
    sql = """SELECT sender, encrypted_message, timestamp
             FROM messages
             WHERE receiver = %s
             ORDER BY timestamp DESC
             LIMIT %s OFFSET %s"""
    cur.execute(sql, (receiver, limit, offset))
    rows = cur.fetchall()
    cur.close()
    db.close()
    return [(sender, decrypt_message(enc), ts) for sender, enc, ts in rows]

if __name__ == "__main__":
    rec = input("Receiver username to fetch messages for: ").strip()
    msgs = get_messages_for_receiver(rec)
    for s, m, t in msgs:
        print(f"{t} | {s} -> {m}")
