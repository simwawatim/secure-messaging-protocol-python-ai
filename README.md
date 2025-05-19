# 🔐 Secure Channel: Encrypted Client-Server Communication using AES-GCM

## 📌 What Happened Before

Initially, a basic client-server Python socket communication setup was created where messages were sent in **plaintext**. However, this approach was **insecure** — any attacker intercepting the messages over the network could easily read them.

To fix this, **AES-GCM encryption** was added to secure the communication. The client now encrypts each message before sending, and the server decrypts the message using a shared secret key.

---

## 🚀 Project Overview

This project demonstrates how to implement **secure socket communication** using **AES-256-GCM** encryption in Python.

- 🔐 **Client** encrypts messages using AES-GCM before sending.
- 🛡️ **Server** decrypts incoming messages using the same key.
- ✅ Communication is now encrypted and more secure.

---

## 🖼️ Screenshots

> Below are some screenshots of the working system:

![Screenshot 1](https://github.com/user-attachments/assets/7660c879-48be-4e93-852c-152c4ede5747)
![Screenshot 2](https://github.com/user-attachments/assets/163d95db-69e8-4d41-b9ae-c885a27f83c5)
![Screenshot 3](https://github.com/user-attachments/assets/421e90ff-9e69-46e2-a32e-724646592e27)
![Screenshot 4](https://github.com/user-attachments/assets/de6cb290-0383-4faf-b62f-6ba1a4ecdaaf)
![Screenshot 5](https://github.com/user-attachments/assets/63d56d0a-9158-4a6f-8cba-f967c63e66d4)
![Screenshot 6](https://github.com/user-attachments/assets/bf27c652-d1b4-4331-b761-1c11e6638cd2)

---

## 📁 Project Structure



---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/secure-channel.git
cd secure-channel


python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


pip install pycryptodome


python server.py
