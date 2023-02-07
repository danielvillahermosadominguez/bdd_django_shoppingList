from shoppinglistapi.shoppinglist.domain.shoppinglist import ShoppingList
from abc import abstractmethod


class ShoppingListRepository:
    @abstractmethod
    def get(self, user) -> ShoppingList:
        pass

    @abstractmethod
    def save(self, shopping_list):
        pass

    @abstractmethod
    def delete(self, user):
        pass
