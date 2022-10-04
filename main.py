from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import pytest
import time

class TestDemoBlaze():
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(service = Service(r"C:\Users\luism\OneDrive\Documentos\AA Trabajos 7to Parcial 22_2\Prueba Aseg Calidad Soft\ChromeDriver\chromedriver.exe"))
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        yield 
        self.driver.quit()

    #Funcion datos para crear e ingresar un Usuario
    def dataUser(self, username_id, password_id):
        user = self.driver.find_element(By.ID, username_id)
        user.send_keys("lmflores") #Nombre de Usuario
        password = self.driver.find_element(By.ID, password_id)
        password.send_keys("paralelepipedo80") #Contraseña

    #----------------Registro---------------#

    def test_signUp(self, setup):
        self.driver.find_element(By.ID, 'signin2').click()
        time.sleep(2)

        self.dataUser("sign-username", "sign-password")
        self.driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]').click()
        time.sleep(2)
        alert = Alert(self.driver)
        alert.accept()
        self.driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[1]/button').click()

    #----------------Ingresar---------------#

    def test_logIn(self, setup):
        self.driver.find_element(By.ID, 'login2').click()
        time.sleep(2)

        self.dataUser("loginusername", "loginpassword")
        self.driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()
        time.sleep(2)

    #----------Agregar al carrito-----------#

    def test_selectProducts(self, setup):
        self.test_logIn(setup)

        articles = {
                    "Phones" : ['//*[@id="tbodyid"]/div[2]/div/div/h4/a', '//*[@id="tbodyid"]/div[5]/div/div/h4/a'],
                    "Laptops" : ['//*[@id="tbodyid"]/div[2]/div/div/h4/a', '//*[@id="tbodyid"]/div[3]/div/div/h4/a'],
                    "Monitors" : ['//*[@id="tbodyid"]/div[1]/div/div/h4/a', '//*[@id="tbodyid"]/div[2]/div/div/h4/a']
                    }
        alert = Alert(self.driver)

        for categories, products in articles.items():
            for product in products:
                time.sleep(2)
                self.driver.find_element(By.LINK_TEXT, categories).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH, product).click()
                time.sleep(1)
                self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
                time.sleep(2)
                alert.accept()
                self.driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[1]/a').click()
        
    #--------Completar el formulario--------#
    
    def test_buyProducts(self, setup):
        self.test_logIn(setup)
        
        time.sleep(2)
        self.driver.find_element(By.ID, 'cartur').click()
        self.driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div/div[2]/button").click()
        time.sleep(2)

        shipping_info = {
                        "name": "Luis Mario",
                        "country": "Mexico",
                        "city": "Queretaro",
                        "card": "1225365278902150",
                        "month": "09",
                        "year": "2022"
                        } 

        for k, v in shipping_info.items():
            data = self.driver.find_element(By.ID, k)
            data.send_keys(v)

        #-----------Comprar Productos-----------#

        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='orderModal']/div/div/div[3]/button[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[10]/div[7]/div/button").click()
        time.sleep(2)

        #--------Cerrar sesion y salir ---------#
        self.driver.find_element(By.XPATH, "//*[@id='logout2']").click()
        time.sleep(2)
