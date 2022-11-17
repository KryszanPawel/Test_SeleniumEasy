import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PATH_TO_DRIVER = "/usr/bin/chromedriver"


class SimpleCheckboxDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(PATH_TO_DRIVER)
        self.driver.get("https://demo.seleniumeasy.com/")
        self.driver.find_element(By.ID, "btn_basic_example").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="basic"]/div/a[2]').click()
        time.sleep(0.5)


    def test_message_is_not_displayed_until_click(self):
        is_message_displayed = self.driver.find_element(By.ID, "txtAge").is_displayed()
        self.assertEqual(is_message_displayed, False)  # message should not be displayed


    def test_checkbox_display_message(self):
        self.driver.find_element(By.ID, "isAgeSelected").click()
        time.sleep(0.2)
        is_message_displayed = self.driver.find_element(By.ID, "txtAge").is_displayed()
        self.assertEqual(is_message_displayed, True)  # message should be displayed

    def test_checkbox_message_disappear_after_unchecking(self):
        box = self.driver.find_element(By.ID, "isAgeSelected")
        box.click()
        time.sleep(0.2)
        box.click()
        is_message_displayed = self.driver.find_element(By.ID, "txtAge").is_displayed()
        self.assertEqual(is_message_displayed, False)  # message should not be displayed

    def tearDown(self):
        self.driver.quit()


class MultipleCheckboxDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH_TO_DRIVER)
        self.driver.get("https://demo.seleniumeasy.com/")
        self.driver.find_element(By.ID, "btn_basic_example").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="basic"]/div/a[2]').click()
        time.sleep(0.5)
        self.list_of_checkboxes = self.driver.find_elements(By.CSS_SELECTOR, ".checkbox label input")[1:]

    def test_start_button_level(self):
        button_text = self.driver.find_element(By.ID, "check1").get_attribute("value")
        self.assertEqual(button_text, "Check All")

    def test_if_all_checkboxes_selected_one_by_one_change_button_label(self):
        for i in self.list_of_checkboxes:
            i.click()
        button_text = self.driver.find_element(By.ID, "check1").get_attribute("value")
        self.assertEqual(button_text, "Uncheck All")

    def test_if_check_all_button_selects_all_checkboxes(self):
        self.driver.find_element(By.ID, "check1").click()
        time.sleep(0.5)
        for i in self.list_of_checkboxes:
            self.assertTrue(i.is_selected())

    def test_if_uncheck_all_button_unselects_all_checkboxes(self):
        self.driver.find_element(By.ID, "check1").click()
        time.sleep(0.5)
        self.driver.find_element(By.ID, "check1").click()
        for i in self.list_of_checkboxes:
            self.assertFalse(i.is_selected())

    def test_if_not_all_boxes_change_button_value(self):
        for i in range(len(self.list_of_checkboxes)):
            self.list_of_checkboxes[i].click()
            button_text = self.driver.find_element(By.ID, "check1").get_attribute("value")
            if i+1 != len(self.list_of_checkboxes):
                self.assertEqual(button_text, "Check All")
            else:
                self.assertEqual(button_text, "Uncheck All")


    def test_if_unchecking_one_box_changing_button_value(self):
        self.driver.find_element(By.ID, "check1").click()
        time.sleep(0.5)
        self.list_of_checkboxes[0].click()
        button_text = self.driver.find_element(By.ID, "check1").get_attribute("value")
        self.assertEqual(button_text, "Check All")


    def test_if_all_checkboxes_on_website_can_be_selected_and_displays_correctly(self):
        self.driver.find_element(By.ID, "isAgeSelected").click()
        for i in self.list_of_checkboxes:
            i.click()
        button_text = self.driver.find_element(By.ID, "check1").get_attribute("value")
        self.assertEqual(button_text, "Uncheck All")

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
