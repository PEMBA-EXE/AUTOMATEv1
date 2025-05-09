import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv  # For environment variables (optional)

# Load environment variables (create a `.env` file for secrets)
load_dotenv()  # Requires `pip install python-dotenv`

# Configure Chrome for Termux (headless)
options = uc.ChromeOptions()
options.add_argument('--headless')  # No GUI needed in Termux
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize undetected ChromeDriver
driver = uc.Chrome(options=options)

def login_to_messenger():
    try:
        driver.get("https://www.messenger.com")
        
        # Wait for login page
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        
        # Fill credentials (use environment variables)
        email = os.getenv("FB_EMAIL") or "your_email@example.com"  # Replace or use .env
        password = os.getenv("FB_PASSWORD") or "your_password"
        
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.ID, "pass").send_keys(password)
        driver.find_element(By.NAME, "login").click()
        
        # Wait for Messenger to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
        )
        print("Login successful! Waiting for messages...")
        
    except Exception as e:
        print(f"Login failed: {e}")
        driver.quit()
        exit()

def auto_reply():
    try:
        # Find latest chat (adjust XPath as needed)
        latest_chat = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@role='row'])[1]"))
        latest_chat.click()
        
        # Send reply
        reply_text = "Hello! This is an automated reply. 😊"
        text_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
        text_box.send_keys(reply_text)
        text_box.send_keys(Keys.RETURN)
        print("Reply sent!")
        
    except Exception as e:
        print(f"Error in auto-reply: {e}")

if __name__ == "__main__":
    login_to_messenger()
    auto_reply()
    time.sleep(3)  # Delay before closing
    driver.quit()
