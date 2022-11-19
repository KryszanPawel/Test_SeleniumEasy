import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PATH_TO_DRIVER = "/usr/bin/chromedriver"


class RadioButtonDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(PATH_TO_DRIVER)
        self.driver.get("https://demo.seleniumeasy.com/")
        self.driver.find_element(By.ID, "btn_basic_example").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="basic"]/div/a[3]').click()
        time.sleep(0.5)
        self.male_button = self.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[1]/div[2]/label[1]')
        self.female_button = self.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[1]/div[2]/label[2]')
        self.get_button = self.driver.find_element(By.ID, 'buttoncheck')
        self.message = self.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[1]/div[2]/p[3]')

    def test_male_option(self):
        self.male_button.click()
        self.get_button.click()

        self.assertFalse(self.female_button.is_selected())
        self.assertEqual(self.message.text, "Radio button 'Male' is checked")

    def test_female_option(self):
        self.female_button.click()
        self.get_button.click()

        self.assertFalse(self.male_button.is_selected())
        self.assertEqual(self.message.text, "Radio button 'Female' is checked")

    def test_change_choice(self):
        self.female_button.click()
        self.get_button.click()

        self.assertFalse(self.male_button.is_selected())
        self.assertEqual(self.message.text, "Radio button 'Female' is checked")

        time.sleep(0.5)

        self.male_button.click()
        self.get_button.click()

        self.assertFalse(self.female_button.is_selected())
        self.assertEqual(self.message.text, "Radio button 'Male' is checked")

    def test_dont_check_anything(self):
        self.get_button.click()

        if 'Male' in self.message.text or 'Female' in self.message.text:
            print(f"Message: {self.message.text}")
            self.assertFalse(True, msg=f"Something is checked")

        else:
            print(f"Message is: {self.message.text}")
            self.assertFalse(False)

    def tearDown(self):
        self.driver.quit()


class GroupRadioButtonsDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH_TO_DRIVER)
        self.driver.get("https://demo.seleniumeasy.com/")
        self.driver.find_element(By.ID, "btn_basic_example").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="basic"]/div/a[3]').click()
        time.sleep(0.5)

        # Buttons
        self.male_button = self.driver.find_element(By.XPATH,
                                                    '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label[1]/'
                                                    'input')
        self.female_button = self.driver.find_element(By.XPATH,
                                                      '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label[2]/'
                                                      'input')
        self.zerofive = self.driver.find_element(By.XPATH,
                                                 '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label[1]/input')
        self.fivefifteen = self.driver.find_element(By.XPATH,
                                                    '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label[2]/'
                                                    'input')
        self.fifteenfifty = self.driver.find_element(By.XPATH,
                                                     '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[2]/label[3]/'
                                                     'input')
        self.get_values = self.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/button')

        # Values
        self.values = self.driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/p[2]')

    def test_dont_make_any_choice(self):
        self.get_values.click()

        self.assertTrue("is not checked" in self.values.text,
                        msg=f"Form does not inform that nothing was checked.\nMessage is: {self.values.text}")

    def test_male_0_to_5(self):
        self.male_button.click()
        self.zerofive.click()
        self.get_values.click()

        self.assertTrue("Male" in self.values.text and "0 - 5" in self.values.text,
                        msg=f"No 'Male' or '0 - 5' in message.\nMessage is: {self.values.text}")

    def test_female_5_to_15(self):
        self.female_button.click()
        self.fivefifteen.click()
        self.get_values.click()

        self.assertTrue("Female" in self.values.text and "5 - 15" in self.values.text,
                        msg=f"No 'Female' or '5 - 15' in message.\nMessage is: {self.values.text}")

    def test_female_15_to_50(self):
        self.female_button.click()
        self.fifteenfifty.click()
        self.get_values.click()

        self.assertTrue("Female" in self.values.text and "15 - 50" in self.values.text,
                        msg=f"No 'Female' or '15 - 50' in message.\nMessage is: {self.values.text}")

    def test_sex_and_no_age_group(self):
        self.female_button.click()
        self.get_values.click()

        self.assertTrue("Female" in self.values.text and ("is not checked" in self.values.text or "choose" in
                                                          self.values.text),
                        msg=f"No 'Female' or form does not inform of unchecked age group..\nMessage is:"
                            f" {self.values.text}")

    def test_sex_not_checked_age_checked(self):
        self.fifteenfifty.click()
        self.get_values.click()

        self.assertTrue("15 - 50" in self.values.text and ("is not checked" in self.values.text or "choose"
                                                           in self.values.text),
                        msg=f"No '15 - 50' or form does not inform of unchecked sex.\nMessage is: {self.values.text}")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
