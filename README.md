# 🤖 Telegram Bot – Software Project Management Assignment

This project implements a **Telegram bot** built in Python, running inside Docker, and consuming the **Binance Public API** to retrieve cryptocurrency prices.  
It was created as part of the *Software Project Management* course.

## 📌 Bot Features

### ✅ 1. `/start` Command
Sends a welcome message and explains available commands.

### ✅ 2. `/precio` (Price) Command
Displays a keyboard with three cryptocurrency options:

- **Bitcoin**
- **Ether**
- **Pepe**

When the user selects one, the bot queries:

```
https://api.binance.com/api/v3/ticker/price?symbol=<SYMBOL>
```

and returns the current price in USDT in a clean, readable format.

### ✅ 3. Automatic Echo
Any message sent by the user that is *not* a command is reflected back:

> User: hello  
> Bot: hello  

### 🔐 4. Secure Token Management via `.env`
The bot token is **not hard‑coded**.  
It is injected through an environment variable using Docker.

### 🐳 5. Fully Dockerized
The bot runs inside a Docker container using:

- Python 3.12 slim  
- requirements.txt dependency installation  
- Long polling (no exposed ports required)  

---

## 🗂️ Project Structure

```
/telegram-bot
│── mi-bot.py
│── requirements.txt
│── Dockerfile
│── .env
│── .dockerignore
│── README.md
```

---

## ⚙️ Installation & Execution

### 1️⃣ Clone the repository

```bash
git clone <repository-url>
cd telegram-bot
```

---

### 2️⃣ Create a `.env` file

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

---

### 3️⃣ Build the Docker image

```bash
docker build -t proyecto:latest .
```

---

### 4️⃣ Run the container

```bash
docker run --name proyecto --env-file .env proyecto:latest
```

You should see:

```
Bot running with long polling...
```

---

## 🧪 How to Interact With the Bot

1. Open Telegram and search for your bot by its **@username**.  
2. Send `/start` → The bot replies.  
3. Send `/precio` → A menu appears with cryptocurrency options.  
4. Select one → The bot fetches the current price from Binance.  
5. Send any other text → The bot echoes it back.

---

## 🌐 External API Used

Binance Public Spot API (no authentication required):

```url
GET https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
```

The response is parsed and formatted for the end user.

---

## 📦 Dependencies (`requirements.txt`)

```
python-telegram-bot>=21.0
requests>=2.0
```

---

## 👤 Author

**Ortega Novoa Octavio**

---

## 📘 Notes

- The bot only works while the Docker container is running.  
- No ports need to be opened thanks to long polling.  