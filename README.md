# SafeTalk 

**SafeTalk** is a real-time, encrypted chat application built using **Python sockets**, **AES encryption**, and **MySQL** for secure message storage and private communication between users.  

---

##  Overview  
SafeTalk is a **terminal-based chat system** designed to ensure **data privacy** and **secure communication**.  
It uses **AES (Advanced Encryption Standard)** to encrypt all messages before transmission and securely store them in a **MySQL database**.  
The application features a **multithreaded server** capable of handling multiple clients simultaneously, enabling smooth and real-time message exchange.  

---

##  Features  
-  AES Encryption (CBC Mode) for secure message transfer  
-  Real-Time Messaging using Python sockets and threading  
-  Encrypted message storage in MySQL  
-  Full-text search and pagination for efficient retrieval  
-  Modular architecture for scalability and easy maintenance  

---

##  Tech Stack  

**Language:** Python  
**Encryption:** AES (PyCryptodome)  
**Database:** MySQL  
**Networking:** Python Socket & Threading  

---

##  How to Run
1. Step 1: install modules
`pip install mysql-connector-python pycryptodome`

2. Step 2: Run setup_db.py file and set up MySQL Database

3. Step 3: AES Encryption & MySQL Connection Run secure_chat_db.py file

4. Step 4: Run store_retrieve.py file

5. Step 5: Start Server i.e. run server.py file

6. Step 6: Once the server starts listening then start Client run client.py file and when the connection is established the message will be shown in the Server and we can enter username in the client file and start messaging

7. Step 7: After everything is done the encrypted message will be stored in the MySQL Database and no one will be able to decrypt the messages easily. 
