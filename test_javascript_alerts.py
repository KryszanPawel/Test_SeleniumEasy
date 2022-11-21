import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time

PATH_TO_DRIVER = "/usr/bin/chromedriver"


class JavaScriptAlertBox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH_TO_DRIVER)
        self.driver.get("https://demo.seleniumeasy.com/")
        self.driver.find_element(By.ID, "btn_basic_example").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="basic"]/div/a[5]').click()
        time.sleep(0.5)
        # Button
        self.click_me = self.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[1]/div[2]/button')

    # Help function to check if alert is dismissed
    def is_alert_dismissed(self):
        try:
            _ = self.driver.switch_to.alert
            return False
        except NoAlertPresentException:
            return True

    def test_close_alert_window(self):
        self.click_me.click()
        alert = self.driver.switch_to.alert
        print(f'Alert: {alert.text}')
        alert.accept()
        # Assert if alert is dismissed
        self.assertTrue(self.is_alert_dismissed())

    def tearDown(self):
        self.driver.quit()


class JavaScriptConfirmBox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH_TO_DRIVER)
        self.driver.get("https://demo.seleniumeasy.com/")
        self.driver.find_element(By.ID, "btn_basic_example").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="basic"]/div/a[5]').click()
        time.sleep(0.5)
        # Button
        self.click_me = self.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/button')

    # Help function to check if alert is dismissed
    def is_alert_dismissed(self):
        try:
            _ = self.driver.switch_to.alert
            return False
        except NoAlertPresentException:
            return True

    def test_click_on_ok_button(self):
        self.click_me.click()
        alert = self.driver.switch_to.alert
        print(f'Alert: {alert.text}')
        alert.accept()

        # Printed message
        self.value = self.driver.find_element(By.ID, 'confirm-demo').text
        # Assert if form printed choice
        self.assertTrue('OK' in self.value)
        # Assert if alert closes
        self.assertTrue(self.is_alert_dismissed())

    def test_click_on_cancel_button(self):
        self.click_me.click()
        alert = self.driver.switch_to.alert
        print(f'Alert: {alert.text}')
        alert.dismiss()

        # Printed message
        self.value = self.driver.find_element(By.ID, 'confirm-demo').text
        # Assert if form printed choice
        self.assertTrue('Cancel' in self.value)
        # Assert if alert closes
        self.assertTrue(self.is_alert_dismissed())

    def tearDown(self):
        self.driver.quit()


class JavaScriptPromptBox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH_TO_DRIVER)
        self.driver.get("https://demo.seleniumeasy.com/")
        self.driver.find_element(By.ID, "btn_basic_example").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="basic"]/div/a[5]').click()
        time.sleep(0.5)
        # Button
        self.click_dor_prompt = self.driver.find_element(By.XPATH,
                                                         '//*[@id="easycont"]/div/div[2]/div[3]/div[2]/button')

    # Help function to check if alert is dismissed
    def is_alert_dismissed(self):
        try:
            _ = self.driver.switch_to.alert
            return False
        except NoAlertPresentException:
            return True

    def test_type_string_and_and_click_on_ok_button(self):
        list_of_inputs = ['Selenium',
                          'Long string with some numbers 1234987654216521568231631275781653716515731527 and dome spe'
                          'cial signs<>?(&^$##łł',
                          'veeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeery long string to test if loooo'
                          'oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong strings are acc'
                          'eptedddddddddddddddddd?',
                          ' random string of signs :hsa d8sa o  s aiodj oaijsdi  iasid8u8ad89asd89asd sda8107*/']

        for string in list_of_inputs:
            self.click_dor_prompt.click()
            alert = self.driver.switch_to.alert
            alert.send_keys(string)
            alert.accept()
            print(list_of_inputs.index(string))
            # Assert if prompt alert is dismissed
            self.assertTrue(self.is_alert_dismissed())
            # Printed message
            value = self.driver.find_element(By.ID, 'prompt-demo').text
            # Assert if typed string is printed
            self.assertEqual(f"You have entered '{string}' !", value)

    def test_click_on_ok_button_without_typing_anything(self):
        self.click_dor_prompt.click()
        alert = self.driver.switch_to.alert
        alert.accept()
        # Assert if prompt alert is dismissed
        self.assertTrue(self.is_alert_dismissed())
        # Printed message
        value = self.driver.find_element(By.ID, 'prompt-demo').text
        # Assert if typed string is printed
        value = value.replace("You have entered ", "")
        value = value.replace(" !", "")
        self.assertEqual('', value, msg="Message should be empty")

    def test_click_on_cancel_button_without_typing_anything(self):
        self.click_dor_prompt.click()
        alert = self.driver.switch_to.alert
        alert.dismiss()
        # Assert if prompt alert is dismissed
        self.assertTrue(self.is_alert_dismissed())
        # Printed message
        value = self.driver.find_element(By.ID, 'prompt-demo').text
        # Assert if typed string is printed
        self.assertEqual('', value, msg="Message should be empty")

    def test_type_string_and_click_on_cancel_button(self):
        self.click_dor_prompt.click()
        alert = self.driver.switch_to.alert
        alert.send_keys("Some String")
        alert.dismiss()
        # Assert if prompt alert is dismissed
        self.assertTrue(self.is_alert_dismissed())
        # Printed message
        value = self.driver.find_element(By.ID, 'prompt-demo').text
        # Assert if typed string is printed
        self.assertEqual('', value, msg="Message should be empty")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
