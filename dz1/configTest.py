import pytest
import yaml
import requests


with open('config.yaml') as file:
    data = yaml.safe_load(file)

url1 = data['url1']
url2 = data['url2']


@pytest.fixture()
def login():
    # Функция получения токена
    obj_data = requests.post(url=url1,
                             data={'username': f'{data["username"]}',
                                   'password': f'{data["password"]}'})
    token = obj_data.json()['token']

    return token


@pytest.fixture()
def create_new_post():
    #Функция создания поста
    obj_data = requests.post(url=url2,
                             headers={"X-Auth-Token": data['token']},
                             data={
                                 'username': f'{data["username"]}',
                                 'password': f'{data["password"]}',
                                 'title': 'data_1',
                                 'description': 'data_2',
                                 'content': 'data_3'})
    return obj_data.json()['description']