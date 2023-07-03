from selenium.webdriver.common.by import By
import time

def Open_web_page(driver):
    driver.get("https://sbis.ru/")
    page_title = driver.title
    assert page_title == "СБИС - экосистема для бизнеса: учет, управление и коммуникации", "Страница не соответсвует ожиданиям"

def Click_on_contacts(driver):
    btn_contacts = driver.find_element(By.XPATH, "//a[@class='sbisru-Header__menu-link sbisru-Header__menu-link--hover' and contains(@href, 'contacts')]")
    time.sleep(3)
    btn_contacts.click()
