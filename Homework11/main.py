from selenium import webdriver
import test_pages_task1.main_sbis_page as main_page
import test_pages_task1.contacts_page as contacts
import test_pages_task1.tensor_page as tensor
import test_pages_task1.about_page as about
import test_pages_task2.auth_fix_page as auth
import test_pages_task2.fix_online_sbis_page as fix_page
import test_data.auth_test_data as data


driver = webdriver.Chrome()


def Run_test_for_task1():
    main_page.Open_web_page(driver)
    main_page.Click_on_contacts(driver)
    contacts.Click_on_tensor_banner(driver)
    tensor.Displayed_block_people_force(driver)
    tensor.Click_on_btn_more(driver)
    about.Check_open_about_page(driver)
    driver.quit()


def Run_test_for_task2():
    auth.Open_auth_page(driver)
    auth.Auth_on_sbis_online_fix(driver, data._INPUT_LOGIN, data._LOGIN)
    auth.Click_on_btn_next_step(driver, data._CHECK_LOGIN)
    auth.Auth_on_sbis_online_fix(driver, data._INPUT_PASSWORD, data._PASSWORD)
    auth.Click_on_btn_next_step(driver, data._CHECK_PASS)
    fix_page.Check_loaded_page(driver)
    fix_page.Move_mouse_on_btn_plus(driver)
    fix_page.Search_contact(driver, "Василенко Вячеслав")
    fix_page.Open_dialog_with_contact(driver, "Василенко Вячеслав")
    fix_page.Write_message_for_contact(driver, "Привет! Я, Славик!")
    fix_page.Send_message(driver)
    fix_page.Click_on_contact(driver)
    fix_page.Open_dialogs(driver)
    fix_page.Is_displayed_message_on_list(driver, "Василенко Вячеслав", "Привет! Я, Славик!")
    fix_page.Remove_message(driver, "Василенко Вячеслав", "Привет! Я, Славик!")
    fix_page.Is_not_displayed_message_on_list(driver, "Василенко Вячеслав", "Привет! Я, Славик!")



Run_test_for_task2()
