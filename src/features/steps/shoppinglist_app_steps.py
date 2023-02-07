import app_utils 
import app_asserts
from behave import fixture, given, then, use_fixture, when
from shoppinglistapi.shoppinglist.domain.shoppinglist import ShoppingList


@given(u'a shopping list application')
def step_impl(context):
    context.user = "USER_1"


@given(u'a shopping list application with {items}')
def step_impl(context, items):
    context.user = "USER_1"
    app_utils.add_items(items, context)


@when(u'add "{items}" in the shopping list application')
def step_impl(context, items):
    app_utils.add_items(items, context)


@when(u'remove "{items}" in the shopping list application')
def step_impl(context, items):
    app_utils.remove_items(items, context)


@then(u'the scenario is ')
def step_impl(context):
    shopping_list = context.application.get(context.user)
    assert(shopping_list.size() == 0)


@then(u'the scenario is {result}')
def step_impl(context, result):
    shopping_list = context.application.get(context.user)
    app_asserts.assert_equal(result, shopping_list)

@when(u'change "{items}" in the shopping list application')
def step_impl(context, items):
    app_utils.change_items(items, context)



