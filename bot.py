from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import traceback
import requests
from dotenv import load_dotenv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load credentials
load_dotenv()
EMAIL = os.getenv("NAUKRI_EMAIL")
PASSWORD = os.getenv("NAUKRI_PASSWORD")

# Telegram credentials (from .env)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_notification(message):
    """Send Telegram notification using bot"""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        params = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
        requests.get(url, params=params)
    except Exception as e:
        print(f"⚠️ Failed to send Telegram notification: {e}")

# Chrome Driver setup
options = Options()
options.add_argument("--start-maximized")
service = Service()
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 20)

try:
    print("🌐 Opening Naukri.com")
    driver.get("https://www.naukri.com/")
    time.sleep(2)

    print("🔐 Logging in")
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']")))
    login_btn.click()
    time.sleep(3)

    email_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']")))
    email_input.send_keys(EMAIL)

    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']")
    password_input.send_keys(PASSWORD)

    login_submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_submit.click()
    time.sleep(5)
    print("✅ Logged in successfully")

    print("➡ Navigating to profile page")
    driver.get("https://www.naukri.com/mnjuser/profile")
    time.sleep(6)

    print("✏️ Scrolling to profile summary section")
    pencil_icon = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//h1[contains(text(),'Profile Summary')]/span[@class='new-pencil']/img")))

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", pencil_icon)
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, -100);")
    pencil_icon.click()
    time.sleep(2)

    print("📝 Editing profile summary text")
    textarea = wait.until(EC.presence_of_element_located((By.ID, "summary")))
    current_text = textarea.get_attribute("value")
    new_text = current_text.strip().rstrip('.') + '.'

    textarea.clear()
    textarea.send_keys(new_text)
    time.sleep(1)

    print("💾 Saving changes")
    save_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))
    save_button.click()
    time.sleep(3)

    print("✅ Profile Summary updated successfully!")
    send_telegram_notification("😎 Bhai Tu Tension Mat Le — Maine Naukri Profile Summary *updated* kar diya hai! ✅🔥")

except Exception as e:
    print("❌ Error occurred:")
    traceback.print_exc()
    send_telegram_notification("🤦‍♂️ Bhai Yr... Naukri Profile update *fail* ho gaya 😭 Shit!! Logs check karle warna HR ka call miss ho jayega! 📞💔")

finally:
    driver.quit()
