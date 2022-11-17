from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

answer_field = browser.find_element(By.ID, "answer")
answer_field.send_keys(y)

button = browser.find_element(By.CLASS_NAME, 'btn')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)


CheckBx = browser.find_element(By.CSS_SELECTOR, '.form-check-custom #robotCheckbox')
CheckBx.click()

RadioBtn = browser.find_element(By.CSS_SELECTOR, '.form-radio-custom #robotsRule')
RadioBtn.click()

time.sleep(1)
button.click()

time.sleep(4)


browser.quit()