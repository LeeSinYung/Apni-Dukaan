# Generated by Selenium IDE
import pytest
import time
import json
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestFormValidation(unittest.TestCase):
  def test_FormValidation(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://sia0.github.io/Apni-Dukaan/")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) > .nav-link").click()
    self.driver.find_element(By.ID, "validationCustom01").click()
    self.driver.find_element(By.ID, "validationCustom01").send_keys("Sia Chong Perng5")
    self.driver.find_element(By.ID, "contactus").click()
    self.driver.implicitly_wait(10)
    nameInput = self.driver.find_element(By.ID, "validationCustom01")
    invalid = "is-invalid" in nameInput.get_attribute("class")
    print(nameInput.get_attribute("class"))
    self.assertTrue(invalid, "Should have display invalid name message")
    self.driver.find_element(By.ID, "validationCustom01").click()
    self.driver.find_element(By.ID, "validationCustom01").send_keys("Sia Chong Perng")
    self.driver.find_element(By.CSS_SELECTOR, ".center-div").click()
    self.driver.find_element(By.CSS_SELECTOR, ".center-div").click()
    nameInput = self.driver.find_element(By.ID, "validationCustom01").get_attribute("class")
    invalid = "is-invalid" in nameInput
    self.assertFalse(invalid, "Should have display invalid name message")
    self.driver.find_element(By.ID, "validationCustom02").click()
    self.driver.find_element(By.ID, "validationCustom02").send_keys("chongperng")
    self.driver.find_element(By.CSS_SELECTOR, ".center-div").click()
    self.driver.find_element(By.ID, "validationCustom02").click()
    self.driver.find_element(By.ID, "validationCustom02").send_keys("chongperngsia@hotmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".center-div").click()
    self.driver.quit()

if __name__ == "__main__":
 unittest.main()