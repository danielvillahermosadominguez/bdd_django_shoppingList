import requests

BASE_URL = "http://localhost:8000"
ITEMS_ENTRY = "items/"
SEPARATOR = "/"
HEALCHECK_ENTRY = "healthcheck"
USER = 'admin'
PASS = 'admin'


def request_get_healthcheck():
    return request_get(HEALCHECK_ENTRY)


def request_get_items():
    return request_get(ITEMS_ENTRY)


def request_delete_item(item, quantity):
    return request_delete(ITEMS_ENTRY + item + SEPARATOR + quantity)


def request_reset_shopping_list():
    data = {"option": "reset"}

    return request_put(ITEMS_ENTRY, data)


def request_delete_all_item():
    return request_delete(ITEMS_ENTRY)


def request_add_item(item):
    return request_post(ITEMS_ENTRY + item + SEPARATOR)


def request_get(endpoint):
    session = requests.Session()
    session.auth = (USER, PASS)
    response = session.get(BASE_URL + SEPARATOR + endpoint)
    return response


def request_update(olditem, newitem):
    return request_put(ITEMS_ENTRY + olditem + SEPARATOR + newitem + SEPARATOR, {})


def request_post(endpoint):
    session = requests.Session()
    session.auth = (USER, PASS)
    response = session.post(BASE_URL+SEPARATOR + endpoint)
    return response


def request_delete(endpoint):
    session = requests.Session()
    session.auth = (USER, PASS)
    response = session.delete(BASE_URL+SEPARATOR + endpoint)
    return response


def request_put(endpoint, data):
    session = requests.Session()
    session.auth = (USER, PASS)
    response = session.put(BASE_URL+SEPARATOR + endpoint,data)
    return response
