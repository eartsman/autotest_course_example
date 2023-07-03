from selenium.webdriver.common.by import By
import time


def Open_auth_page(driver):
    driver.get("https://fix-online.sbis.ru/")
    page_title = driver.title
    assert page_title == "Вход в личный кабинет", "Страница не соответсвует ожиданиям"

def Auth_on_sbis_online_fix(driver, input_name, text):
    time.sleep(3)
    input_for_enter_login_and_password = driver.find_element(By.XPATH, f"//input[@name='{input_name}']")
    input_for_enter_login_and_password.send_keys(text)


def Click_on_btn_next_step(driver, part_attribute_in_btn):
    part_for_xpath = "auth-AdaptiveLoginForm__"
    btn_accept = driver.find_element(By.XPATH, f"//span[@data-qa='{part_for_xpath}{part_attribute_in_btn}']")
    if btn_accept.is_displayed():
        btn_accept.click()
    else:
        raise Exception("Кнопка для подтверждения логина/пароля не найдена!")

