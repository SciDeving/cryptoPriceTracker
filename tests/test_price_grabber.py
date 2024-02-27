from os import environ

import pytest
from dotenv import dotenv_values
from requests import Response

from src.crypto_price_tracker import price_grabber as system_under_test

key_path_url = environ["BASE_URL"] + environ["KEY_PATH"]


@pytest.fixture(scope="module")
def setup_class():
    dotenv_values(".env")
    dotenv_values(".env.secret")


def test_connect_to_coin_market_cap():
    assert system_under_test.session != None
    assert system_under_test.session.get(environ["BASE_URL"] + environ["KEY_PATH"])
    assert type(system_under_test.session.get(key_path_url)) is Response
    assert system_under_test.session.get(key_path_url).status_code == 200
