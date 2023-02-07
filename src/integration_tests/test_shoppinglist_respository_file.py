import unittest
from shoppinglistapi.shoppinglist.infra.shoppinglistrepositoryFile import ShoppingListRepositoryFile
from shoppinglistapi.shoppinglist.domain.shoppinglist import ShoppingList
import os
import json
import shutil


class ShoppingListRespositoryTest(unittest.TestCase):

    DATA_FOLDER = "./data/"

    def test_save_ShoppingList(self):
        # Arrange
        repository = ShoppingListRepositoryFile()
        shopping_list1 = ShoppingList("user1")
        shopping_list1.add("Bread")
        shopping_list1.add("Milk")
        shopping_list1.add("Onion")

        shopping_list2 = ShoppingList("user2")
        shopping_list2.add("Peper")
        shopping_list2.add("Yogurt")
        shopping_list2.add("Tomatoe")

        # Act
        repository.save(shopping_list1)

        # Assert
        self._assert_exist_file_with_data(
            self.DATA_FOLDER, self.DATA_FOLDER + "user1.json", shopping_list1)

        # Act
        repository.save(shopping_list2)

        # Assert
        self._assert_exist_file_with_data(
            self.DATA_FOLDER, self.DATA_FOLDER + "user2.json", shopping_list2)

    def setup_method(self, method):
        if(os.path.exists(self.DATA_FOLDER)):
            shutil.rmtree(self.DATA_FOLDER)

    def test_recover_ShoppingList(self):
        # Arrange
        repository = ShoppingListRepositoryFile()
        shopping_list1 = repository.get("user1")
        shopping_list1.add("Bread")
        shopping_list1.add("Milk")
        shopping_list1.add("Onion")
        repository.save(shopping_list1)
        shopping_list2 = repository.get("user2")
        shopping_list2.add("Peper")
        shopping_list2.add("Yogurt")
        shopping_list2.add("Tomatoe")
        repository.save(shopping_list2)

        # Act
        shopping_list_recovered = repository.get("user1")

        # Assert
        self.assertTrue(isinstance(shopping_list_recovered, ShoppingList))
        self._assert_equals_shoppingLists(shopping_list1, shopping_list_recovered)

        # Act
        shopping_list_recovered = repository.get("user2")

        # Assert
        self.assertTrue(isinstance(shopping_list_recovered, ShoppingList))
        self._assert_equals_shoppingLists(shopping_list2, shopping_list_recovered)

    def _assert_exist_file_with_data(self, folder, file, shopping_list):
        data = json.dumps(shopping_list.__dict__)
        self.assertTrue(os.path.exists(folder))
        self.assertTrue(os.path.exists(file))
        file = open(file, "r")
        file_text = file.read()
        file.close()
        self.assertEqual(data, file_text)

    def _assert_equals_shoppingLists(self, sl1, sl2):
        data1 = json.dumps(sl1.__dict__)
        data2 = json.dumps(sl2.__dict__)
        self.assertEquals(data1, data2)
