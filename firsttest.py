from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

assert driver.title == "Web form"

text_box = driver.find_element(By.NAME, "my-text")
text_box.send_keys("Selenium")

driver.find_element(By.CSS_SELECTOR, "button").click()

message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "message"))
)

print(message.text)

assert message.text == "Received!"
driver.quit()
