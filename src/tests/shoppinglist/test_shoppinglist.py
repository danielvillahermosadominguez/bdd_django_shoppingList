import unittest
import pytest
from shoppinglistapi.shoppinglist.domain.shopping_list_errors import ItemNotFoundError
from shoppinglistapi.shoppinglist.application.shoppinglist_appserv import ShoppingListAppServ
from .spy_repository import ShoppingListRepositorySpy


class ShoppingListServiceTest(unittest.TestCase):
    BREAD = "bread"
    MILK = "milk"
    ONION = "onion"
    USER_NAME_1 = "user1"

    def setUp(self):
        self.repository = ShoppingListRepositorySpy()
        self.sut = ShoppingListAppServ(self.repository)

    def tearDow
    def test_it_should_add_an_item(self):
        # Act
        self.sut.add(self.BREAD, self.USER_NAME_1)

        # Assert
        self._assert_added_and_is_the_only_one(
            self.sut, self.USER_NAME_1, self.BREAD)
        self._assert_repo_contain_only(self.USER_NAME_1, self.BREAD, 1)

    def test_it_should_change_an_item_with_other(self):
        # Arrange
        self.sut.add(self.BREAD, self.USER_NAME_1)
        self.sut.add(self.MILK, self.USER_NAME_1)
        # Act
        self.sut.change(self.MILK, self.ONION, self.USER_NAME_1)
        # Assert
        shoppingList = self.sut.get(self.USER_NAME_1)
        self.assertEqual(2, shoppingList.size())
        self.assertEqual(1, shoppingList.get_item_quantity(0))
        self.assertEqual(1, shoppingList.get_item_quantity(1))
        self.assertEqual(self.BREAD, shoppingList.get_item_description(0))
        self.assertEqual(self.ONION, shoppingList.get_item_description(1))

        self.assertEqual(1, len(self.repository.get_dic()))

    def test_when_delete_fail_it_should_throw_exception(self):
        # Act
        with pytest.raises(ItemNotFoundError):
            self.sut.delete(self.MILK, 1, self.USER_NAME_1)

    def test_it_should_remove_an_item(self):

        # Arrange
        self.sut.add(self.BREAD, self.USER_NAME_1)
        self.sut.add(self.BREAD, self.USER_NAME_1)
        self.sut.add(self.MILK, self.USER_NAME_1)

        # Act
        self.sut.delete(self.MILK, 1, self.USER_NAME_1)

        # Assert
        shopping_list = self.sut.get(self.USER_NAME_1)
        self._assert_shopping_list_contain_only(shopping_list, self.BREAD, 2)
        self._assert_repo_contain_only(self.USER_NAME_1, self.BREAD, 2)

    def test_it_should_remove_all_items(self):

        # Arrange
        self.sut.add(self.BREAD, self.USER_NAME_1)
        self.sut.add(self.BREAD, self.USER_NAME_1)
        self.sut.add(self.MILK, self.USER_NAME_1)

        # Act
        self.sut.delete_all(self.USER_NAME_1)

        # Assert
        self.assertEqual(0, len(self.repository.get_dic()))
        shopping_list = self.sut.get(self.USER_NAME_1)
        self.assertEqual(0, shopping_list.size())

    def test_it_should_reset_all_items(self):
        # Arrange
        self.sut.add(self.BREAD, self.USER_NAME_1)
        self.sut.add(self.BREAD, self.USER_NAME_1)
        self.sut.add(self.MILK, self.USER_NAME_1)
        self.sut.add(self.MILK, self.USER_NAME_1)
        self.sut.add(self.MILK, self.USER_NAME_1)

        # Act
        self.sut.reset(self.USER_NAME_1)

        # Assert
        shopping_list = self.sut.get(self.USER_NAME_1)
        self._assert_bread_and_milk_reset(shopping_list, self.USER_NAME_1)
        self._assert_repo_has_been_called_and_shoppingList_reset()

    def _assert_repo_has_been_called_and_shoppingList_reset(self):
        dic = self.repository.get_dic()
        self.assertEqual(1, len(dic))
        self.assertEqual(self.BREAD, dic[self.USER_NAME_1].get_item_description(0))
        self.assertEqual(1, dic[self.USER_NAME_1].get_item_quantity(0))
        self.assertEqual(self.MILK, dic[self.USER_NAME_1].get_item_description(1))
        self.assertEqual(1, dic[self.USER_NAME_1].get_item_quantity(1))

    def _assert_bread_and_milk_reset(self, shopping_list, user_name):
        self.assertEqual(2, shopping_list.size())
        self.assertEqual(self.BREAD, shopping_list.get_item_description(0))
        self.assertEqual(1, shopping_list.get_item_quantity(0))
        self.assertEqual(self.MILK, shopping_list.get_item_description(1))
        self.assertEqual(1, shopping_list.get_item_quantity(1))

    def _assert_added_and_is_the_only_one(self, sut, user_name, item):
        result = sut.get(user_name)
        self.assertEqual(1, result.size())
        self.assertEqual(item, result.get_item_description(0))
        self.assertEqual(1, result.get_item_quantity(0))

    def _assert_repo_contain_only(self, user_name, item, quantity):
        dic = self.repository.get_dic()
        self.assertEqual(1, len(dic.keys()))
        self.assertEqual(dic[user_name].get_item_description(0), item)
        self.assertEqual(dic[user_name].get_item_quantity(0), quantity)

    def _assert_shopping_list_contain_only(self, shopping_list, item, quantity):
        self.assertEqual(1, shopping_list.size())
        self.assertEqual(item, shopping_list.get_item_description(0))
        self.assertEqual(quantity, shopping_list.get_item_quantity(0))
