from selenium import webdriver
import math
import time
import unittest


class TestA(unittest.TestCase):
    
	def test_1(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)
		
		first_name = browser.find_element_by_xpath("//label[contains(text(), 'First name')]/../input")
		first_name.send_keys("Ivan")
		last_name = browser.find_element_by_xpath("//label[contains(text(), 'Last name')]/../input")
		last_name.send_keys("Ivanov")
		email = browser.find_element_by_xpath("//label[contains(text(), 'Email')]/../input")
		email.send_keys("mail")

		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		time.sleep(1)

		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text

		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error")

	def test_2(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)
		
		first_name = browser.find_element_by_xpath("//label[contains(text(), 'First name')]/../input")
		first_name.send_keys("Ivan")
		last_name = browser.find_element_by_xpath("//label[contains(text(), 'Last name')]/../input")
		last_name.send_keys("Ivanov")
		email = browser.find_element_by_xpath("//label[contains(text(), 'Email')]/../input")
		email.send_keys("mail")

		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		time.sleep(1)

		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text

		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error")

if __name__ == "__main__":
    unittest.main()