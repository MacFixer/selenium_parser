import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base64 import b64decode
from PIL import Image
import pytesseract
from io import BytesIO


class AvitoParser:

    def setUp(self):
        self.driver =webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(8)
        driver.get("https://www.avito.ru/krasnodar/predlozheniya_uslug/krasota_zdorove-ASgBAgICAUSYC6qfAQ?q=%D0%BD%D0%B0%D1%80%D0%B0%D1%89%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5+%D1%80%D0%B5%D1%81%D0%BD%D0%B8%D1%86")

        try:
            elems = driver.find_elements_by_class_name("item__line")
            wait = WebDriverWait(driver, 60)

            for key, elem in enumerate(elems):

                if key == 4:
                    break

                title_elem = elem.find_element_by_class_name("snippet-title")
                title_text = title_elem.text
                hover = ActionChains(driver).move_to_element(elem)
                price_str = elem.find_element_by_class_name("snippet-price-row").text
                district = elem.find_element_by_class_name("item-address-georeferences-item__content").text
                hover.perform()
                phone_button = elem.find_element_by_class_name("js-item-extended-contacts.button-origin").click()

                rand_sleep = random.randint(12, 19)
                print(rand_sleep/10)
                time.sleep(rand_sleep/10)

                # wait.until(EC.visibility_of_element_located((By.TAG_NAME, "button"))).click()

                # tel_img = elem.find_element_by_class_name("item-extended-phone")

                # tel_img = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "item-extended-phone"))).get_attribute('src')

                # tel_image = elem
                print(title_text, end="")
                print(district, end="")
                # print(tel_img, end="")
                print(price_str, end="\n")
                # time.sleep(1)

            phone_pictures = driver.find_elements_by_class_name("item-extended-phone")
            for pict in phone_pictures:
                phone_pict = pict.get_attribute('src')
                data = b64decode(phone_pict.split('base64,')[-1].strip())
                temp_buff = BytesIO()
                temp_buff.write(data)
                temp_buff.seek(0)
                image = Image.open(temp_buff)

                print(pytesseract.image_to_string(image))

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


