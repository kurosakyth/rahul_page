import pytest
import json
import selenium.webdriver
@pytest.fixture
def config(scope='session'):
    with open('config.json') as config_file:
        config = json.load(config_file)
    return config

@pytest.fixture
def browser(config):
    if config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
    b.implicitly_wait(config['implicit_wait'])
    yield b
    b.quit()