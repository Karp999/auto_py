# Задание 1.
# Добавить в задание с REST API ещё один тест, в котором создаётся новый пост, 
# а потом проверяется его наличие на сервере по полю «описание».

# Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts 
# с передачей параметров title, description, content.

import requests
import yaml
import pytest

with open('config.yaml') as file:
    data = yaml.safe_load(file)

url1 = data['url1']
url2 = data['url2']
website = 'https://test-stand.gb.ru/api/posts'
username = f'{data["username"]}'
password = f'{data["password"]}'


def token_auth(token):
    res = requests.get(url=data["url2"],
                       headers={"X-Auth-Token": token},
                       params={"owner": "notMe"})
    content = [item["content"] for item in res.json()['data']]
    return content

def test_step1(login):
    assert '' in token_auth(login)

def test_step2(create_new_post):
    assert 'data_2' in create_new_post
