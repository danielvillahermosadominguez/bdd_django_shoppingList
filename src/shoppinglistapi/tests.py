from django.test import TestCase
from shoppinglistapi.shoppinglist.infra.shoppinglistrepositoryDJANGODB import ShoppingListRepositoryDJANGODB
from shoppinglistapi.shoppinglist.domain.shoppinglist import ShoppingList
import os
# Strategy: No news, good news
class ShoppingListRespositoryDJANGO(TestCase):
    
    def test_save_ShoppingList(self):
        # Arrange
        repository = ShoppingListRepositoryDJANGODB()
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
       

        # Act
        repository.save(shopping_list2)

        # Assert
       
    def setup_method(self, method):
      os.remove("./db_test.sqlite3")

    def test_recover_ShoppingList(self):
        # Arrange
        repository = ShoppingListRepositoryDJANGODB()
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
        
        # Act
        shopping_list_recovered = repository.get("user2")

        # Assert
        
    