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

class Testing(unittest.TestCase):
    def test_navigationBar(self):
        self.driver = webdriver.Chrome()  
        url = "https://sia0.github.io/Apni-Dukaan/stationery.html"
        self.driver.get(url)
        self.driver.set_window_size(1296, 705)
        self.driver.find_element(By.XPATH, "//a[contains(@href, './index.html')]").click()
        self.driver.get(url)
        self.driver.find_element(By.LINK_TEXT, "Offers").click()
        self.driver.get(url)
        self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) > .nav-link").click()
        self.driver.get(url)
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.get(url)
        self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(5) > .nav-link").click()
        self.driver.get(url)
        self.driver.find_element(By.LINK_TEXT, "FAQ").click()
        self.driver.get(url)
        self.driver.find_element(By.ID, "navbarDropdown").click()
        self.driver.find_element(By.LINK_TEXT, "Mobile").click()
        self.driver.get(url)
        self.driver.find_element(By.ID, "navbarDropdown").click()
        self.driver.find_element(By.LINK_TEXT, "TV/Appliances").click()
        self.driver.get(url)
        self.driver.find_element(By.ID, "navbarDropdown").click()
        self.driver.find_element(By.LINK_TEXT, "Furniture").click()
        self.driver.get(url)
        self.driver.find_element(By.ID, "navbarDropdown").click()
        self.driver.find_element(By.LINK_TEXT, "Baby/Kids").click()
        self.driver.get(url)
        self.driver.find_element(By.ID, "navbarDropdown").click()
        self.driver.find_element(By.LINK_TEXT, "Login/Signup").click()
        self.driver.get(url)
        self.driver.find_element(By.ID, "navbarDropdown").click()
        self.driver.find_element(By.LINK_TEXT, "Stationery").click()
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main()

