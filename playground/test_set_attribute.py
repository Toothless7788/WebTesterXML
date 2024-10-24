"""
Created on 21/2/2024 by w45242hy
Last-edit: 21/2/2024 by w45242hy
The programme to test amend element's attributes using selenium
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
    element = web_driver.find_element(By.XPATH, "//div[@id='msg']")
    print("element = ", element)

    """
    2 methods: 
    1. self.__web_driver.execute_script("arguments[0].value = ...", element)  # It works
    2. self.__web_driver.execute_script("document.getElementById() ...")  # It works
    """
    web_driver.execute_script(
        "arguments[0].value = 'Bye, this is created by execute_script()'", element)
    # web_driver.execute_script(
    #     "document.getElementById('msg').value = 'Hello, this is created by execute_script()';")

    element = web_driver.find_element(By.ID, "msg")
    print(f"element.value = {element.get_attribute('value')}")

    time.sleep(1)

    web_driver.quit()

    print("Programme finished ...")
