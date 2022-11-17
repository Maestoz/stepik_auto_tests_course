from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")
time.sleep(2)
elements = browser.find_elements(By.CSS_SELECTOR, 'input[type]')
time.sleep(2)
for element in elements:
    element.send_keys("123")
time.sleep(2)
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()


# успеваем скопировать код за 30 секунд
time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла
