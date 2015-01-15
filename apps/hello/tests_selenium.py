# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# from django.core.urlresolvers import reverse

# from django.contrib.sites.models import Site

# from django.test.client import RequestFactory

# import urlparse
# import selenium

# class AdminEditFormTest(unittest.TestCase):
#     """
#     test data is saved
#     """

#     def setUp(self):        
#         self.driver = webdriver.Firefox()
#         self.url = "http://127.0.0.1:8000/"

#     def testUserEsditsDataCorrect(self):
#         """ test when user enters correct data """
#         self.driver.get(self.url)
#         assert "Main Page" in self.driver.title
#         elem = self.driver.find_element_by_name("edit_page_link")
#         elem.click()
#         assert "Edit Page" in self.driver.title
#         elem = self.driver.find_element_by_name("user-first_name")
#         elem.clear()
#         elem.send_keys("NewValue")
#         elem = self.driver.find_element_by_name("save_and_back_submit")
#         elem.click()
#         assert "Main Page" in self.driver.title
#         assert "Name: NewValue" in self.driver.page_source
        

#     def testUserEsditsDataCorrect(self):
#         """ test when user enters INcorrect data """
#         self.driver.get(self.url)
#         assert "Main Page" in self.driver.title
#         elem = self.driver.find_element_by_name("edit_page_link")
#         elem.click()
#         assert "Edit Page" in self.driver.title
#         elem = self.driver.find_element_by_name("user-email")
#         elem.clear()
#         elem.send_keys("BadEmail")
#         elem = self.driver.find_element_by_name("save_and_back_submit")
#         elem.click()
#         assert "Edit Page" in self.driver.title
        
#     def tearDown(self):
#         self.driver.close()




# if __name__ == "__main__":
#     unittest.main()
