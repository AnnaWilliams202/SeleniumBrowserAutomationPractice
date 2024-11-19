from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



username = 'tomsmith'
password = 'SuperSecretPassword!'
website_url = 'https://the-internet.herokuapp.com/login'
chromedriver_path = 'chromedriver-mac-arm64/chromedriver'


chrome_options = Options()
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service ,options=chrome_options)
driver.get(website_url)

username_field = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'username')))
password_field = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'password')))
login_button = driver. find_element (By. CSS_SELECTOR, '#login >button > i')

username_field.send_keys('tomsmith')
password_field.send_keys('SuperSecretPassword!')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#login > button > i'))
).click()

# You can now perform other actions on the website as anauthenticated user
# For example, you can get the page title to verify login success
print("Page title after login:", driver.title)

 #The browser will remain open for manual inspection
input("Press Enter to close the browser...")



driver.quit()


