import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH_TO_DRIVER = "/usr/bin/chromedriver"


class SelectListDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH_TO_DRIVER)
        self.driver.get("https://demo.seleniumeasy.com/")
        self.driver.find_element(By.ID, "btn_basic_example").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="basic"]/div/a[4]').click()
        time.sleep(0.5)
        # Dropdown
        self.dropdown = self.driver.find_element(By.ID, "select-demo")
        self.select = Select(self.dropdown)
        self.options = self.select.options
        self.options = [day.text for day in self.options]
        # Value label
        self.value = self.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[1]/div[2]/p[2]')

    def test_if_Please_select_is_selectable(self):
        self.assertFalse(self.driver.find_element(By.XPATH, '//*[@id="select-demo"]/option[1]').is_enabled())

    def test_if_values_in_dropdown_print_correct_message(self):
        options = self.options[1:]
        for item in options:
            self.select.select_by_value(item)
            self.assertEqual(self.value.text.replace("Day selected :- ", ""), item)

    def tearDown(self):
        self.driver.quit()


class MultiSelectListDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH_TO_DRIVER)
        self.driver.get("https://demo.seleniumeasy.com/")
        self.driver.find_element(By.ID, "btn_basic_example").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="basic"]/div/a[4]').click()
        time.sleep(0.5)
        # List
        self.list = self.driver.find_element(By.ID, "multi-select")
        self.select = Select(self.list)
        self.options = self.select.options
        # Value label
        self.value = self.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/p[2]')
        # Buttons
        self.first_selected = self.driver.find_element(By.ID, 'printMe')
        self.all_selected = self.driver.find_element(By.ID, 'printAll')

    def test_none_selected(self):
        # Assert first selected
        self.first_selected.click()
        result = self.value.text
        self.assertTrue("undefined" in result or "none" in result)
        # Assert all selected
        self.all_selected.click()
        result = self.value.text
        self.assertTrue("undefined" in result or "none" in result, msg=f"Message displayed does not inform about "
                                                                       f"nothing selected. Message: '{result}'")

    def test_one_selected(self):
        self.options = [country.text for country in self.options]
        checkvalue = self.options[3]
        self.select.select_by_value(checkvalue)
        # Assert first selected
        self.first_selected.click()
        self.assertEqual(self.value.text.replace('First selected option is : ', ''), checkvalue)
        # Assert all selected
        self.all_selected.click()
        self.assertEqual(self.value.text.replace('Options selected are : ', ''), checkvalue)

    def test_three_selected(self):
        list_of_chosen = [self.options[-1], self.options[0], self.options[4]]
        action = ActionChains(self.driver)
        action.move_to_element(self.list)
        for i in list_of_chosen:
            action.key_down(Keys.CONTROL)
            action.click(i)
            action.key_up(Keys.CONTROL)
            action.perform()
        # Assert first selected
        self.first_selected.click()
        self.assertEqual(self.value.text.replace('First selected option is : ', ''), list_of_chosen[0].text)
        # Assert all selected
        self.all_selected.click()
        final_string = 'Options selected are : '
        for state in list_of_chosen:
            final_string += state.text
            if state != list_of_chosen[-1]:
                final_string += ','
        self.assertEqual(self.value.text, final_string)

    def test_all_selected(self):
        list_of_chosen = self.options
        action = ActionChains(self.driver)
        action.move_to_element(self.list)
        for i in list_of_chosen:
            action.key_down(Keys.CONTROL)
            action.click(i)
            action.key_up(Keys.CONTROL)
            action.perform()
        # Assert first selected
        self.first_selected.click()
        self.assertEqual(self.value.text.replace('First selected option is : ', ''), list_of_chosen[0].text)
        # Assert all selected
        self.all_selected.click()
        final_string = 'Options selected are : '
        for state in list_of_chosen:
            final_string += state.text
            if state != list_of_chosen[-1]:
                final_string += ','
        self.assertEqual(self.value.text, final_string)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
