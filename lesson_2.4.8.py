from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button1 = browser.find_element_by_id("book")
    button1.click()
    x = browser.find_element_by_id("input_value")
    x = x.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button2 = browser.find_element_by_id("solve")
    button2.click()

finally:
    browser.quit
 
