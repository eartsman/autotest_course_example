import time


def Check_open_about_page(driver):
    time.sleep(5)
    url_about_page = driver.current_url
    assert url_about_page == "https://tensor.ru/about", f"URL старницы не соответствует ожиданиям: {url_about_page}"
