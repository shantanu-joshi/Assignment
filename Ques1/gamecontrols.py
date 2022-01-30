from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


path = r'C:\Users\shant\Downloads\chromedriver.exe'

driver = webdriver.Chrome(path)
driver.get('https://now.gg/apps/perfect-world/7724/perfect-world-mobile.html')
driver.maximize_window()

driver.find_element_by_xpath("//button[@lang='en']").click()



element = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.ID, "video-footer-btn")))
element.click()


driver.implicitly_wait(10)


name =driver.find_element_by_xpath("//div[@class='tab-content keyboard']/ul[2]")
name2 = driver.find_element_by_xpath("//div[@class='tab-body']")


textocopied = name2.text

file1 = open('Commands.txt', 'w')
file1.write(textocopied)





