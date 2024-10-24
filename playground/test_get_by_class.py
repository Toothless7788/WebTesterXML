"""
Created on 18/2/2024 by w45242hy
Last-edit: 18/2/2024 by w45242hy
The programme to test get element by class.NAME using selenium
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

url = "https://mdn.github.io/dom-examples/indexeddb-api/index.html"

if __name__ == "__main__":
    # Main programme
    web_driver = webdriver.Chrome()
    web_driver.set_page_load_timeout(20)
    web_driver.get(url)

    # Fill in the form to prompt error message
    element = web_driver.find_element(By.ID, "add-button")
    element.click()

    print("Button is clicked ...")
    time.sleep(3)

    # Error message should be prompted

    # Method 1: First find <div>, then find the element inside
    # element = web_driver.find_element(By.ID, "msg")
    # print(f"element = {element}")
    # element2 = element.find_element(By.CLASS_NAME, "action-failure")
    # print(f"element2 = {element2}")
    # print(f"element2.text = {element2.text}")

    # Method 2: Find <span class="action-failure"> directly
    # Not working. Probably different versions of selenium
    element = web_driver.find_element(By.CLASS_NAME, "action-failure")
    print(f"element.text = {element.text}")

    web_driver.quit()

    print("Main programme finished ...")
