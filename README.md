## 🚀 Naukri Profile Updater (with Telegram Notifications)

### 📌 About the Project

This Python automation script **logs into Naukri.com**, goes to your **profile page**, and updates the **Profile Summary** automatically.
It’s designed to keep your Naukri profile **fresh & active** (boosting visibility for recruiters 👀).

✅ Bonus Feature: It also sends you a **real-time Telegram notification** when the profile update is successful (or if it fails).


### ⚡ Features

* 🔐 Secure login using credentials from `.env` file
* 📝 Auto-update your **Profile Summary**
* 📩 Sends **Telegram notifications** on success/failure
* 🤖 Keeps your Naukri profile **active daily**
* 🛡️ Credentials & tokens are not hardcoded (safe for GitHub)


### 🛠️ Tech Stack

* **Python 3**
* **Selenium** (for automation)
* **Python-dotenv** (for environment variables)
* **Requests** (for Telegram API)


### 📂 Project Setup

1. **Clone this repo**

   ```bash
   git clone https://github.com/cyberfortify/naukri-profile-updater.git
   cd naukri-profile-updater
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Setup `.env` file**
   Create a `.env` file in root directory with your credentials:

   ```
   NAUKRI_EMAIL=your-email@example.com
   NAUKRI_PASSWORD=your-naukri-password

   TELEGRAM_TOKEN=your-telegram-bot-token
   TELEGRAM_CHAT_ID=your-chat-id
   ```

4. **Run the script**

   ```bash
   python bot.py
   ```



### 📲 Telegram Notification Preview

* ✅ Success:
  *"😎 Bhai Tu Tension Mat Le — Maine Naukri Profile Summary updated kar diya hai! 🔥"*

* ❌ Failure:
  *"🤦‍♂️ Bhai Yr... Naukri Profile update fail ho gaya 😭 Logs check kar le warna HR ka call miss ho jayega!"*


### 🔮 Future Enhancements

* Auto-update **Resume file** regularly 📄
* Add **email notifications** (SMTP / Gmail API) ✉️
* Integration with **cron jobs** or GitHub Actions for scheduling ⏰


### 📜 License

This project is **open-source** and free to use under the MIT License.
