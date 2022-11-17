from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

PATH_TO_DRIVER = "/usr/bin/chromedriver"


class SingleInputFieldTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH_TO_DRIVER)

        self.driver.get("https://demo.seleniumeasy.com/")

        start_button = self.driver.find_element(By.ID, 'btn_basic_example')
        start_button.click()
        time.sleep(1)

    def test_single_word(self):
        self.test_message = "New"


    def test_string(self):
        self.test_message = "New message 123"

    def test_long_string(self):
        self.test_message = "This is some long string to test if long strings work as intended. " \
                            "Sometimes it can cut the end of a string"

    def test_long_string_with_special_signs(self):
        self.test_message = "Again lets test long string with some numbers and special signs (123456.,';[)." \
                            " Let me make it a bit longer please."

    def test_random_string_of_characters(self):
        self.test_message = "srdtfyhijksdatfsa6t  8sta 6dt 6sdabsdhsad7  asyd6adasdas  sada" \
                            "h fa654s19d98as as kjs auig sa ih sad"


    def tearDown(self):

        simple_form_demo = self.driver.find_element(By.XPATH, '//*[@id="basic"]/div/a[1]')
        simple_form_demo.click()

        single_form = self.driver.find_element(By.ID, 'user-message')
        single_form.send_keys(self.test_message)

        show_message_button = self.driver.find_element(By.CSS_SELECTOR, '#get-input button')
        show_message_button.click()

        return_message = self.driver.find_element(By.ID, 'display').text

        self.assertEqual(self.test_message, return_message)
        self.driver.quit()


class TwoInputFields(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH_TO_DRIVER)

        self.driver.get("https://demo.seleniumeasy.com/")

        start_button = self.driver.find_element(By.ID, 'btn_basic_example')
        start_button.click()
        time.sleep(1)

    def test_two_zeros(self):
        self.value_1, self.value_2 = 0, 0

    def test_two_integers(self):
        self.value_1, self.value_2 = 1, 7

    def test_two_large_numbers(self):
        self.value_1, self.value_2 = 2000000000001, 1000000000025

    def test_two_floats(self):
        self.value_1, self.value_2 = 1.1, 5.75

    def test_two_stings(self):
        self.value_1, self.value_2 = "test", "text"

    def test_one_string_one_number(self):
        self.value_1, self.value_2 = 17, "text"

    def tearDown(self):

        if not isinstance(self.value_1,str) and not isinstance(self.value_2, str):
            total = str(self.value_1 + self.value_2)

        else:
            total = "NaN"

        self.driver.find_element(By.XPATH, '//*[@id="basic"]/div/a[1]').click()

        self.driver.find_element(By.ID, 'sum1').send_keys(self.value_1)

        self.driver.find_element(By.ID, 'sum2').send_keys(self.value_2)

        self.driver.find_element(By.CSS_SELECTOR, '#gettotal button').click()

        get_total = self.driver.find_element(By.ID, 'displayvalue').text

        self.assertEqual(get_total, total)

        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
