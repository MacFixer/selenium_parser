import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AvitoParser:

    def setUp(self):
        self.driver =webdriver.Chrome()
        driver = self.driver
        driver.get("https://www.avito.ru/krasnodar/predlozheniya_uslug/krasota_zdorove-ASgBAgICAUSYC6qfAQ?q=%D0%BD%D0%B0%D1%80%D0%B0%D1%89%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5+%D1%80%D0%B5%D1%81%D0%BD%D0%B8%D1%86")

        try:
            elems = driver.find_elements_by_class_name("item__line")
            # elems = driver.find_elements_by_class_name("item_table-wrapper")

            wait = WebDriverWait(driver, 20)

            for elem in elems:

                title_elem = elem.find_element_by_class_name("snippet-title")
                title_text = title_elem.text
                hover = ActionChains(driver).move_to_element(elem)
                hover.perform()

                price_str = elem.find_element_by_class_name("snippet-price-row").text
                phone_button = elem.find_element_by_class_name("js-item_table-extended-contacts")
                wait.until(EC.visibility_of_element_located((By.TAG_NAME, "button"))).click()

                # tel_img = elem.find_element_by_class_name("item-extended-phone")

                # tel_image = elem
                print(title_text, end="")
                # print(tel_img, end="")
                print(price_str, end="\n")
                # time.sleep(1)

            # hover = ActionChains(driver).move_to_element(elem)
            # hover.perform()
            # elem.send_keys("pycon")
            # elem.send_keys(Keys.RETURN)
            # assert "No results found." not in driver.page_source

        finally:
            driver.quit()

if __name__ == "__main__":
    driver = AvitoParser()
    driver.setUp()
