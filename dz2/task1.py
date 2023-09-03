# Задание №1:
# Добавить в наш тестовый проект шаг добавления поста после входа. 
# Должна выполняться проверка на наличие названия поста на странице сразу после его создания.


import time
import yaml
from module import ChromeSite

with open("testdata.yaml") as f: 
    testdata = yaml.safe_load(f)

site = ChromeSite(testdata["address"])

def test_step():
    # Шаги:
    # 1. Авторизация,
    # 2. Создание поста,
    # 3. Заполнение полей,
    # 4. Сохранение информации,
    # 5. Тестирование создание поста.
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys("tresBian9")
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys("poloko36")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()

    time.sleep(3)

    x_selector1 = """//*[@id="create-btn"]"""
    input1 = site.find_element("xpath", x_selector1)
    input1.click()

    time.sleep(3)

    x_selector1 = """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("Field_Title")
    x_selector2 = """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("Field_Description")
    x_selector3 = """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""
    input3 = site.find_element("xpath", x_selector3)
    input3.send_keys("Field_Content")

    time.sleep(3)

    x_selector4 = """//*[@id="create-item"]/div/div/div[7]/div/button/span"""
    input4 = site.find_element("xpath", x_selector4)
    input4.click()

    time.sleep(3)

    x_selector_x = """//*[@id="app"]/main/div/div[1]/h1"""
    text_label = site.find_element("xpath", x_selector_x)
    assert text_label.text == 'Field_Title'
