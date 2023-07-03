from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


def Displayed_block_people_force(driver):
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    block_news = driver.find_element(By.XPATH, "//div[@class='tensor_ru-Index__block4-content tensor_ru-Index__card']")
    ActionChains(driver) \
        .scroll_to_element(block_news) \
        .perform()
    time.sleep(5)
    assert block_news.is_displayed(), "блок новости 'Сила в людях' присутствует на странице"


def Click_on_btn_more(driver):
    btn_more = driver.find_element(By.XPATH, "//a[@class='tensor_ru-link tensor_ru-Index__link' and contains(@href, 'about')]")
    btn_more.click()