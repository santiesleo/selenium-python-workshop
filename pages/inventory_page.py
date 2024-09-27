from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, 'inventory_list')

    def is_inventory_page_displayed(self):
        return self.find_element(self.TITLE).is_displayed()
