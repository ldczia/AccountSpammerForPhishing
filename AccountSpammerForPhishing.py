import pyautogui
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChomeDriverManager().install()), options=options)

url = ''
driver.get(url)
time.sleep(10)
login_btn = WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable((By.ID, 'login-btn')))
login_btn.click()

email_field = WebDriverWait(driver, timeout=10).until(EC_presence_of_element_located((By.ID, 'email')))
pass_field = driver.find_element(By.ID, value='password')
pass_field.send_keys('rinarpzia')

words = ['rinarpzia1', 'konusmaaq', 'gaddbicaklanmis', 'jaxeysusamq', 'enissusanayi', 'plataoplomo']

while True:
    kelime = random.choice(words)
    email_field.send_keys(word)
    email_field.clear()
    email_field.submit()