from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\luism\OneDrive\Documentos\AA Trabajos 7to Parcial 22_2\Prueba Aseg Calidad Soft\ChromeDriver\chromedriver.exe")
driver.get("https://www.demoblaze.com/index.html")
driver.maximize_window()
alert = Alert(driver)

def dataUser(username_id, password_id):
    user = driver.find_element(By.ID, username_id)
    user.send_keys("lmflores")
    password = driver.find_element(By.ID, password_id)
    password.send_keys("paralelepipedo80")

#----------------Registro---------------#

# driver.find_element(By.ID, 'signin2').click()
# time.sleep(2)

# dataUser("sign-username", "sign-password")
# driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]').click()
# time.sleep(3)
# alert.accept()
# driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[1]/button').click()

#----------------Ingresar---------------#

driver.find_element(By.ID, 'login2').click()
time.sleep(2)

dataUser("loginusername", "loginpassword")
driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()
time.sleep(2)

#----------Agregar al carrito-----------#

articles = {
            "Phones" : ['//*[@id="tbodyid"]/div[2]/div/div/h4/a', '//*[@id="tbodyid"]/div[5]/div/div/h4/a'],
            "Laptops" : ['//*[@id="tbodyid"]/div[2]/div/div/h4/a', '//*[@id="tbodyid"]/div[3]/div/div/h4/a'],
            "Monitors" : ['//*[@id="tbodyid"]/div[1]/div/div/h4/a', '//*[@id="tbodyid"]/div[2]/div/div/h4/a']
            }

# for categories, products in articles.items():
#     for product in products:
#         time.sleep(2)
#         driver.find_element(By.LINK_TEXT, categories).click()
#         time.sleep(2)
#         driver.find_element(By.XPATH, product).click()
#         time.sleep(2)
#         driver.find_element(By.LINK_TEXT, "Add to cart").click()
#         time.sleep(3)
#         alert.accept()
#         driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[1]/a').click()

time.sleep(2)
driver.find_element(By.LINK_TEXT, 'Phones').click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[2]/div/div/h4/a").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Add to cart").click()
time.sleep(3)
alert.accept()
driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[1]/a').click()

#-------------Ir al carrito-------------#

time.sleep(2)
driver.find_element(By.ID, 'cartur').click()

#--------Completar el formulario--------#

driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div/div[2]/button").click()
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
    data = driver.find_element(By.ID, k)
    data.send_keys(v)

time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='orderModal']/div/div/div[3]/button[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[10]/div[7]/div/button").click()
time.sleep(2)

#--------Cerrar sesion y salir ---------#

driver.find_element(By.XPATH, "//*[@id='logout2']").click()
time.sleep(2)
driver.quit()
