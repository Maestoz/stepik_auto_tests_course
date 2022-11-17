from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/file_input.html"
browser.get(link)
name = browser.find_element(By.NAME, "firstname")
name.send_keys("name")
last = browser.find_element(By.NAME, "lastname")
last.send_keys("last")
ema = browser.find_element(By.NAME, "email")
ema.send_keys("asd@asd.com")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'test.txt') # добавляем к этому пути имя файла 
    
browsefile = browser.find_element(By.NAME, "file")       
browsefile.send_keys(file_path)
submit = browser.find_element(By.CLASS_NAME, "btn")
submit.click()

time.sleep(10)



browser.quit()