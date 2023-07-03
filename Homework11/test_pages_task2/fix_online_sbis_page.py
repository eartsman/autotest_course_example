from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def Check_loaded_page(driver):
    url_page = "https://fix-online.sbis.ru/"
    time.sleep(10)
    assert url_page == driver.current_url, "URL загруженной страницы не совпадает с ожиданияем!"


def Click_on_contact(driver):
    time.sleep(5)
    btn_contact = driver.find_element(By.XPATH, "//span[@data-qa='NavigationPanels-Accordion__title' and text()='Контакты']")
    if btn_contact.is_displayed():
        btn_contact.click()
    else:
        raise Exception("Контакты отсутствуют в списке")


def Open_dialogs(driver):
    time.sleep(5)
    btn_contact_on_inner_menu = driver.find_element(By.XPATH, "//a[@name='headTitle' and contains(@href, '/page/dialogs')]")
    if btn_contact_on_inner_menu.is_displayed():
        btn_contact_on_inner_menu.click()
    else:
        raise Exception("Контакты отсутствуют в списке")


def Move_mouse_on_btn_plus(driver):
    btn_for_mouse_move = driver.find_element(By.XPATH, "//a[@data-name='contacts']//span[@data-qa='NavigationPanels-Accordion__icon']")
    move = ActionChains(driver).move_to_element(btn_for_mouse_move).click()
    move.perform()
    time.sleep(10)


def Search_contact(driver, contact_name):
    search = driver.find_element(By.XPATH, "//div[@class='controls-StackTemplate-content_wrapper controls-StackTemplate_backgroundColor']/descendant::input")
    search.send_keys(contact_name)


def Open_dialog_with_contact(driver, contact_name):
    time.sleep(10)
    current_contact_in_list = driver.find_element(By.XPATH, f"//div[@class='msg-addressee-item']/descendant::span[@data-qa='person-Information__fio' and text()='{contact_name}']")
    if current_contact_in_list.is_displayed():
        current_contact_in_list.click()
    else:
        raise Exception(f"Контакт с именем {contact_name} в списке не найден!")


def Write_message_for_contact(driver, message):
    time.sleep(10)
    text_area_for_message = driver.find_element(By.XPATH, "//div[@data-qa='textEditor_slate_Field']")
    if text_area_for_message.is_displayed():
        text_area_for_message.send_keys(message)
    else:
        raise Exception("Текстовое поле для ввода сообщения не найдено!")


def Send_message(driver):
    btn_send_message = driver.find_element(By.XPATH, "//span[@data-qa='msg-send-editor__send-button']")
    time.sleep(5)
    if btn_send_message.is_displayed():
        btn_send_message.click()
        time.sleep(5)
    else:
        raise Exception("Кнопка для отправки сообщения не найдена!")


def Is_displayed_message_on_list(driver, contact_name, text_message):
    time.sleep(5)
    contact_message = driver.find_element(By.XPATH, f"//div[@data-qa='controls-Scroll__content']//div[@name='viewContainer']//div[@data-qa='items-container']//div[@data-qa='msg-dialogs-item__addressee' and text()='{contact_name}']//..//..//p[contains(text(), '{text_message}')]")
    assert contact_message.is_displayed(), "Сообщение в реестре не отобразилось!"


def Remove_message(driver, contact_name, text_message):
    time.sleep(5)
    contact_message = driver.find_element(By.XPATH, f"//div[@data-qa='controls-Scroll__content']//div[@name='viewContainer']//div[@data-qa='items-container']//div[@data-qa='msg-dialogs-item__addressee' and text()='{contact_name}']//..//..//p[contains(text(), '{text_message}')]")
    remove = ActionChains(driver).move_to_element(contact_message).context_click()
    remove.perform()
    time.sleep(3)
    btn_remove = driver.find_element(By.XPATH, "//div[@data-qa='item']/descendant::div[@class='ws-ellipsis controls-Menu__content-wrapper_width' and text()='Удалить']")
    r = ActionChains(driver).move_to_element(btn_remove).click()
    r.perform()


def Is_not_displayed_message_on_list(driver, contact_name, text_message):
    time.sleep(5)
    contact_message = driver.find_element(By.XPATH, f"//div[@data-qa='controls-Scroll__content']//div[@name='viewContainer']//div[@data-qa='items-container']//div[@data-qa='msg-dialogs-item__addressee' and text()='{contact_name}']//..//..//p[contains(text(), '{text_message}')]")
    if contact_message.is_displayed():
        raise Exception("Сообщение не удалилось!")





