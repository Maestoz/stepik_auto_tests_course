from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

time.sleep(1)

firstbtn = browser.find_element(By.CSS_SELECTOR, '.container .btn')
firstbtn.click()

redir = browser.window_handles[1]
old = browser.window_handles[0]
browser.switch_to.window(redir)


x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)


answer_field = browser.find_element(By.ID, "answer")
answer_field.send_keys(y)


Submit = browser.find_element(By.CLASS_NAME, 'btn')
Submit.click()

time.sleep(4)




browser.quit()

