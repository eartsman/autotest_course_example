from selenium.webdriver.common.by import By
import time


def Click_on_tensor_banner(driver):
    time.sleep(5)
    banner = driver.find_element(By.XPATH, "//a[@class='sbisru-Contacts__logo-tensor mb-8' and contains(@href, 'tensor.ru')]")
    banner.click()