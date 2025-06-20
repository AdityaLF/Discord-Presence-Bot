# Discord Presence Bot

A simple yet powerful Discord bot built with Python using the `discord.py` library. It dynamically sets a streaming activity displaying live total member and server counts.

<img src="https://i.ibb.co/xtv0cvDB/image.png" width="400" />

---

## ✨ Features

* **📊 Dynamic Status** — Displays real-time totals of members and servers directly in the bot's streaming activity status.
* **🎮 Custom Presence** — Sets a rich streaming activity with a YouTube/Twitch URL.

---

## 🚀 Setup & Installation

Follow the steps below to run this bot on your own server.

### 1. Prerequisites

* **Python 3.8+** — [Download here](https://www.python.org/downloads/)
* **pip** — Comes with Python
* **Git** — [Download here](https://git-scm.com/downloads)

### 2. Create Bot & Get Required Info

#### Create a Discord Bot Application

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"**, give it a name
3. Navigate to the **"Bot"** tab, click **"Add Bot"**, then confirm

#### Obtain Bot Token

1. Still under the **"Bot"** tab, click **"Reset Token"** to get your bot token
2. **Store it securely** — Never share it publicly

#### Enable Privileged Intents

* Under the **"Bot"** tab, scroll to **"Privileged Gateway Intents"**
* Enable both:

  * **PRESENCE INTENT**
  * **SERVER MEMBERS INTENT**

### 3. Clone the Repository

Open your terminal or command prompt:

```bash
git clone https://github.com/AdityaLF/Discord-Presence-Bot.git
cd Discord-Presence-Bot
```

### 4. Configure the Bot Token

Replace `'bot_token_here'` in the code with your actual bot token:

```python
YOUR_BOT_TOKEN = 'bot_token_here'
```

### 5. Run the Bot

After saving your changes and ensuring dependencies are installed, run the bot with:

```bash
python bot.py
```

---

## 👤 Author

* **GitHub**: [@AdityaLF](https://github.com/AdityaLF)
* **Discord**: [@05.07am](https://discordapp.com/users/786163564205047839)
* **Support Me**: [ko-fi.com/adityaf](https://ko-fi.com/adityaf)

---

## 📄 License

This project is licensed under the **MIT License** — you are free to use, modify, and share this project.
