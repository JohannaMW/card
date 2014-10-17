# __author__ = 'johanna'
# from time import sleep
#
# from django.core.urlresolvers import reverse
# from django.test import LiveServerTestCase
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.webdriver import WebDriver
# from ..models import Player
#
#
# class SeleniumTests(LiveServerTestCase):
#         @classmethod
#         def setUpClass(cls):
#             cls.selenium = WebDriver()
#             super(SeleniumTests, cls).setUpClass()
#
#         @classmethod
#         def tearDownClass(cls):
#             cls.selenium.quit()
#             super(SeleniumTests, cls).tearDownClass()
#
#         def test_user_login(self):
#             # Create User
#             Player.objects.create_user(username='test-user', email='test@test.com', password='password')
#             # open login
#             self.selenium.get("{}{}".format(self.live_server_url, reverse('login')))
#             self.selenium.find_element_by_name('username').send_keys('test-user')
#             password_input = self.selenium.find_element_by_name('password')
#             password_input.send_keys('password')
#             password_input.send_keys(Keys.RETURN)
#             sleep(.10)
#
#             #self.selenium.find_element_by_name("Login").click()
#
#         def test_admin_login(self):
#             # Create a superuser
#             Player.objects.create_superuser('superuser', 'superuser@test.com', 'mypassword')
#
#             # let's open the admin login page
#             self.selenium.get("{}{}".format(self.live_server_url, reverse('admin:index')))
#             # let's fill out the form with our superuser's username and password
#             self.selenium.find_element_by_name('username').send_keys('superuser')
#             password_input = self.selenium.find_element_by_name('password')
#             password_input.send_keys('mypassword')
#
#             # Submit the form
#             password_input.send_keys(Keys.RETURN)
#             # sleep for half a second to let the page load
#             sleep(.10)
#
#             #We check to see if 'Site administration' is now on the page, this means we logged in successfully
#             body = self.selenium.find_element_by_tag_name('body')
#             self.assertIn('Site administration', body.text)
#
#         def admin_login(self):
#             # Create a superuser
#             Player.objects.create_superuser('superuser', 'superuser@test.com', 'mypassword')
#
#             # let's open the admin login page
#             self.selenium.get("{}{}".format(self.live_server_url, reverse('admin:index')))
#
#             # let's fill out the form with our superuser's username and password
#             self.selenium.find_element_by_name('username').send_keys('superuser')
#             password_input = self.selenium.find_element_by_name('password')
#             password_input.send_keys('mypassword')
#
#             # Submit the form
#             password_input.send_keys(Keys.RETURN)
#
#         def test_admin_new_player(self):
#             self.admin_login()
#             self.selenium.find_elements_by_link_text('Users')[0].click()
#             self.selenium.find_element_by_link_text('Add user').click()
#             self.selenium.find_element_by_name('password').send_keys("password")
#             self.selenium.find_element_by_name('username').send_keys("test_user")
#             self.selenium.find_element_by_name('phone').send_keys("650-111-2222")
#             self.selenium.find_element_by_css_selector("input[value='Save']").click()
#             sleep(.5)
#
#         def admin_new_player(self):
#             self.admin_login()
#             self.selenium.find_elements_by_link_text('Users')[0].click()
#             self.selenium.find_element_by_link_text('Add user').click()
#             self.selenium.find_element_by_name('password').send_keys("password")
#             self.selenium.find_element_by_name('username').send_keys("test_user")
#             self.selenium.find_element_by_name('phone').send_keys("650-111-2222")
#             self.selenium.find_element_by_css_selector("input[value='Save']").click()
#             sleep(.5)
#
#         # def test_admin_edit_player(self):
#         #     self.admin_new_player()
#         #     self.selenium.find_elements_by_link_text('Users')[0].click()
#
#         def test_admin_create_card(self):
#             self.admin_login()
#
#             # We can check that our Card model is registered with the admin and we can click on it
#             # Get the 2nd one, since the first is the header
#             self.selenium.find_elements_by_link_text('Cards')[1].click()
#
#             # Let's click to add a new card
#             self.selenium.find_element_by_link_text('Add card').click()
#             # Let's fill out the card form
#             self.selenium.find_element_by_name('rank').send_keys("ace")
#             suit_dropdown = self.selenium.find_element_by_name('suit')
#             for option in suit_dropdown.find_elements_by_tag_name('option'):
#                 if option.text == "heart":
#                     option.click()
#
#             # Click save to create the new card
#             self.selenium.find_element_by_css_selector("input[value='Save']").click()
#
#             sleep(.5)
#
#             # Check to see we get the card was added success message
#             body = self.selenium.find_element_by_tag_name('body')
#             self.assertIn('The card "ace of hearts" was added successfully', body.text)