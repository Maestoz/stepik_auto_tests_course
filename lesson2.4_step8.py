from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = browser.find_element(By.ID, "book")



# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

button.click()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

answer_field = browser.find_element(By.ID, "answer")
answer_field.send_keys(y)


Submit = browser.find_element(By.ID, "solve")
Submit.click()

time.sleep(7)
browser.quit()



