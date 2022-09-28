from selenium import webdriver
#from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
#from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\luism\OneDrive\Documentos\AA Trabajos 7to Parcial 22_2\Prueba Aseg Calidad Soft\ChromeDriver\chromedriver.exe")
driver.get("https://www.demoblaze.com/index.html")
driver.maximize_window()
alert = Alert(driver)

#----------------Registro---------------#

driver.find_element(By.ID, 'signin2').click()
time.sleep(2)

user = driver.find_element(By.ID, "sign-username")
user.send_keys("lmflores")
password = driver.find_element(By.ID, "sign-password")
password.send_keys("paralelepipedo80")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]').click()
time.sleep(2)
alert.accept()
driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[1]/button').click()

#----------------Ingresar---------------#

driver.find_element(By.ID, 'login2').click()
time.sleep(2)

user = driver.find_element(By.ID, "loginusername")
user.send_keys("lmflores")
password = driver.find_element(By.ID, "loginpassword")
password.send_keys("paralelepipedo80")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()
time.sleep(2)
#driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[1]/button').click()

#----------Agregar al carrito-----------#

articles = {'Phones': ['//*[@id="tbodyid"]/div[2]/div/div/h4/a', '//*[@id="tbodyid"]/div[5]/div/div/h4/a'],
            'Laptops': ['//*[@id="tbodyid"]/div[2]/div/div/h4/a', '//*[@id="tbodyid"]/div[3]/div/div/h4/a'],
            'Monitors': ['//*[@id="tbodyid"]/div[1]/div/div/h4/a', '//*[@id="tbodyid"]/div[2]/div/div/h4/a']}

driver.find_element(By.LINK_TEXT, ).click()
driver.find_element(By.XPATH, ).click()
