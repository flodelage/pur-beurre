
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui


class HomeSearchTest(LiveServerTestCase):

  def test_home_search(self):
    driver = webdriver.Chrome('/Users/floriandelage/Downloads/chromedriver')
    driver.get('http://127.0.0.1:8000/')
    wait = ui.WebDriverWait(driver, 1000)
    search_form = driver.find_element_by_id('id_search')

    #populate the form with data
    search_form.send_keys('Nutella')

    #submit form
    search_form.send_keys(Keys.RETURN)

    assert 'http://127.0.0.1:8000/catalog/products/' in driver.current_url
    # wait.until(lambda driver: driver.find_element_by_tag_name("iframe").is_displayed())

    #check result; page source looks at entire html document
    assert 'Nutella' in driver.page_source
