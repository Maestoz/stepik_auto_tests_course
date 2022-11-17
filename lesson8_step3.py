from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

time.sleep(1)

x1 = browser.find_element(By.ID, "num1")
x2 = browser.find_element(By.ID, "num2")
intx1 = int(x1.text)
intx2 = int(x2.text)
sum = intx1+intx2
strsum = str(sum)


select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(strsum)

Submit = browser.find_element(By.CLASS_NAME, 'btn')
Submit.click()

time.sleep(4)


browser.quit()