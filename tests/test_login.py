import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestLogin(unittest.TestCase):

    def setUp(self):
        """
        Método que se ejecuta antes de cada prueba. Aquí se inicializa el navegador.
        """
        self.driver = webdriver.Chrome()  # o webdriver.Firefox()
        self.driver.get("https://www.saucedemo.com/v1/index.html")
        self.login_page = LoginPage(self.driver)

    def test_login_success(self):
        """
        Prueba para verificar que un usuario puede iniciar sesión con credenciales válidas.
        """
        self.login_page.login("standard_user", "secret_sauce")
        inventory_page = InventoryPage(self.driver)
        self.assertTrue(inventory_page.is_inventory_page_displayed(), "El usuario no fue redirigido a la página de inventario")

    def test_login_failure(self):
        """
        Prueba para verificar que el login falla con credenciales incorrectas.
        """
        self.login_page.login("invalid_user", "invalid_password")
        error_message = self.login_page.find_element((By.CSS_SELECTOR, ".error-message-container")).text
        self.assertIn("Epic sadface", error_message, "El mensaje de error no se mostró como se esperaba")

    def test_login_empty_credentials(self):
        """
        Prueba para verificar que el login falla cuando se envían credenciales vacías.
        """
        self.login_page.login("", "")
        error_message = self.login_page.find_element((By.CSS_SELECTOR, ".error-message-container")).text
        self.assertIn("Epic sadface", error_message, "El mensaje de error no se mostró como se esperaba")

    def tearDown(self):
        """
        Método que se ejecuta después de cada prueba. Cierra el navegador.
        """
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
