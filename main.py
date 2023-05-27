from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time 

_cred:map = {
    "user" : "user",
    "pass" : "pass"
}


def _trv_exc(driver):
   return driver.execute_script("document.getElementsByClassName('_3GDyz0bgwoWgoxYSYSxXyA _3SalNr9zKm9cow28G6Et8k')[0].scrollTo(0,0)\n"
         + "document.getElementsByClassName('_3GDyz0bgwoWgoxYSYSxXyA _3SalNr9zKm9cow28G6Et8k')[0].dispatchEvent(new WheelEvent('wheel'))")

def _trv_n():
    _t_options = webdriver.ChromeOptions()
    _t_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=_t_options)
    driver.get("")
    driver.find_element(By.XPATH, '/html/body/div/main/div[1]/div/div[2]/form/fieldset[1]/input').send_keys(_cred["user"])
    driver.find_element(By.XPATH, '//*[@id="loginPassword"]').send_keys(_cred["pass"])
    driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button").submit()
    if WebDriverWait(driver, timeout = 3).until(driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/div[1]/div[2]/div[1]/div[1]/div")):
        driver.implicitly_wait(7)
        while True:
           _trv_exc(driver)
           time.sleep(0.2) 

if __name__ == "__main__":
    _trv_n()
