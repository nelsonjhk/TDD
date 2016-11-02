from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase): 

	def setUp(self): 
		self.browser = webdriver.Chrome()

	def tearDown(self): 
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self): # methods that begin with "test" will be run"
		#This isn't a recipe app yet, just a to-do list. but nevertheless it must be accessed.
		self.browser.get('http://localhost:8000') # Attempt to open homepage

		# Look at title; am I where I'm supposed to be? 
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')
		# The list is there. Enter an item. 

		# Type in "Meet NaNo Word Count" into text box

		# When enter is hit, the page updates, and now the page lists "1. Meet NaNo Word Count" as an item in the list. 
		# There is still a text box for next item. Enter "Take notes on Sipser." Press return key. 

		# Page updates once more, and both items are shown. 


		# Note the page's unique URL; an explanation should be present. 

		# Visiting unique URL should restore her list. 

		# All done for the day. 

	
if __name__ == '__main__': 
	unittest.main(warnings='ignore')
