from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User opens up the homepage for the To-Do list
        self.browser.get('http://localhost:8000')

        # User sees the page title and header mention To-Do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test!")
        
        # User is invited to enter a to-do item straight away

        # User types "Buy peacock feathers" into a text box

        # When the user hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting the user to add another item.
        # User enters "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on the list

        # User wonders if the site will remember the list.  Sees that the site
        # has generated a unique URL -- there is some explanatory text to that effect.

        # User visits that URL - the to-do list is still there

if __name__ == '__main__':
    unittest.main(warnings='ignore')