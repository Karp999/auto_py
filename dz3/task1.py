# Задание 1:
# Добавить в проект тест по проверке механики работы формы Contact Us на главной странице личного кабинета. 
# Должно проверятся открытие формы, ввод данных в поля, клик по кнопке и появление всплывающего alert.

import time
import pytest
from pageTest import OperationHelper
username = "tresBian9"
password = "poloko36"

def test_step_1(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login("tresBian9")
    test_page1.enter_pswd("poloko36")
    test_page1.click_button()
    time.sleep(3)
#Вход
    test_page1.click_contact()
    time.sleep(3)
#Заполнение полей
    test_page1.enter_cont_name("tresBian9")
    test_page1.enter_cont_email("monte@mail.ru")
    test_page1.enter_cont_text("bon bon")
    time.sleep(1)
    test_page1.click_button()
    time.sleep(1)
#Проверка всплывающего окна
    assert test_page1.get_alert_text() == "Форма успешно отправлена!"