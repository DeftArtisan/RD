from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

_cred:map = {
    "user" : "Uroboros6",
    "pass" : "rexonA123"
}

def _trv_exc(driver):
   return driver.execute_script("document.getElementsByClassName('_3GDyz0bgwoWgoxYSYSxXyA _3SalNr9zKm9cow28G6Et8k')[0].scrollTo(0,0);document.getElementsByClassName('_3GDyz0bgwoWgoxYSYSxXyA _3SalNr9zKm9cow28G6Et8k')[0].dispatchEvent(new WheelEvent('wheel'))")

def _trv_n():
    _t_options = webdriver.ChromeOptions()
    _t_options.add_experimental_option("detach", True)
    _d = DesiredCapabilities.CHROME
    _d['goog:loggingPrefs'] = { 'browser':'ALL' } 
    driver = webdriver.Chrome(options=_t_options, desired_capabilities=_d)
    driver.get("https://www.reddit.com/chat/channel/1384089_98c13592595ab2be501ccc9cc6947cf26eb3bcf5")
    driver.find_element(By.XPATH, '/html/body/div/main/div[1]/div/div[2]/form/fieldset[1]/input').send_keys(_cred["user"])
    driver.find_element(By.XPATH, '//*[@id="loginPassword"]').send_keys(_cred["pass"])
    driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button").submit()
    if WebDriverWait(driver, timeout = 3).until(driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/div[1]/div[2]/div[1]/div[1]/div")):
         driver.implicitly_wait(7)
         while True:
             if "Uncaught (in promise) SendBirdException: Query in progress." in str(driver.get_log("browser")):
                  driver.refresh()
                  time.sleep(3)
        _trv_exc(driver)
        time.sleep(0.2) 

if __name__ == "__main__":
    _trv_n()
