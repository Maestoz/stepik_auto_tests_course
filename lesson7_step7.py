from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

time.sleep(1)

x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

time.sleep(1)

answer_field = browser.find_element(By.ID, "answer")
answer_field.send_keys(y)

CheckBx = browser.find_element(By.ID, "robotCheckbox")
CheckBx.click()

RadioBtn = browser.find_element(By.ID, "robotsRule")
RadioBtn.click()

Submit = browser.find_element(By.CLASS_NAME, 'btn')
Submit.click()

time.sleep(4)


browser.quit()