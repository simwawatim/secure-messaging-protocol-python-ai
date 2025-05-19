# 🔐 Secure Channel: Encrypted Client-Server Communication using AES-GCM

## 📌 What Happened Before

Initially, a basic client-server Python socket communication setup was created, where messages were sent in plaintext. However, this approach was insecure — anyone intercepting the messages over the network could read the contents.

To address this, **AES-GCM encryption** was introduced to secure the communication. The client now encrypts messages before sending them, and the server decrypts them using a shared secret key.

---

## 🚀 Project Overview

This project demonstrates how to implement **secure socket communication** using **AES-256-GCM** in Python. Messages sent from the client are encrypted before transmission and decrypted by the server upon receipt.


![Scre![Screenshot from 2025-05-19 09-54-59](https://github.com/user-attachments/assets/7660c879-48be-4e93-852c-152c4ede5747)
enshot from 2025-05-19 09-54-45](https://github.com/user-attachments/assets/163d95db-69e8-4d41-b9ae-c885a27f83c5)

---

## 📁 Project Structure

