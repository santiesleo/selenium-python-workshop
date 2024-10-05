from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardIntuPage(BasePage):
    SEARCH_FIELD = (By.CSS_SELECTOR, '[data-action="search"]')
    
    def is_search_displayed(self):
        return self.find_element(self.SEARCH_FIELD).is_displayed()