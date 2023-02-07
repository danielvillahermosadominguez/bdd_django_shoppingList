import json
import os
from http import HTTPStatus

import requests

from behave import fixture, given, then, use_fixture, when
from behave.fixture import fixture_call_params, use_fixture_by_tag

from shoppinglist_asserts import (assert_is_equal,
                                  assert_not_correct_format,
                                  assert_ok,
                                  assert_there_is_nothing_to_delete,
                                  assert_the_name_not_exist)
from shoppinglist_proxy import (request_delete,
                                request_get,
                                request_get_items,
                                request_post,
                                request_get_healthcheck,
                                request_add_item,
                                request_delete_item,
                                request_delete_all_item,
                                request_update,
                                request_reset_shopping_list)
from utils import kill, remove_folder, run_server


@given(u'a shopping list')
def step_impl(context):
    set_empty_shopping_list()


@given(u'a shopping list with the following items')
def step_impl(context):
    set_empty_shopping_list()
    add_items(context)


@when(u'ask if the shopping list is alive')
def step_impl(context):
    context.response = request_get_healthcheck()


@when(u'add "{item}" in the shopping list')
def step_impl(context, item):
    context.response = request_add_item(item)


@when(u'add "" in the shopping list')
def step_impl(context):
    context.response = request_add_item("")


@when(u'remove {quantity} item of "{item}"')
def step_impl(context, quantity, item):
    context.response = request_delete_item(item, quantity)


@when(u'remove all items')
def step_impl(context):
    context.response = request_delete_all_item()

@when(u'change the item "{olditem}" with "{newitem}"')
def step_impl(context, olditem, newitem):
    context.response = request_update(olditem,newitem)
    print("prueba")

@when(u'reset the quantity of all items')
def step_impl(context):
    context.response = request_reset_shopping_list()

@then(u'the shopping list is empty')
def step_impl(context):
    response = request_get_items()
    assert_ok(response)
    json_data = json.loads(response.content)
    assert(len(json_data['_dict']) == 0)

@then(u'the shopping list is alive')
def step_impl(context):
    assert_ok(context.response)


@then(u'the shopping list has')
def step_impl(context):
    response = request_get_items()
    assert_ok(response)
    json_data = json.loads(response.content)
    assert_is_equal(json_data['_dict'], context.table)


@then(u'you cannot add a item with a no correct format')
def step_impl(context):
    assert_not_correct_format(context.response)


@then(u'it is impossible to remove this quantity in this items')
def step_impl(context):
    assert_there_is_nothing_to_delete(context.response)

@then(u'the name doesn\'t exist')
def step_impl(context):
    assert_the_name_not_exist(context.response)

def set_empty_shopping_list():
    request_delete_all_item()
    
# auxiliar funtions: add


def add_n_items(context, item, n):
    for i in range(0, n):
        context.request = request_add_item(item)


def add_items(context):
    for row in context.table:
        item = row['Item']
        quantity = int(row['Quantity'])
        add_n_items(context, item, quantity)
