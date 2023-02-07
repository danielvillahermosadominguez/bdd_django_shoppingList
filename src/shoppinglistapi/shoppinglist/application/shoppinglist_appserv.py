from shoppinglistapi.shoppinglist.domain.shoppinglist import ShoppingList
from shoppinglistapi.shoppinglist.domain.shopping_list_errors import  ItemNotFoundError

class ShoppingListAppServ:
    def __init__(self, repository):
        self._list = []
        self._repository = repository

    def add(self, item, user):
        shopping_list = self.get(user)
        shopping_list.add(item)
        self._repository.save(shopping_list)
    
    def change(self, olditem, newitem, user):
        shopping_list = self.get(user)
        shopping_list.change(olditem, newitem)
        self._repository.save(shopping_list)

    def delete(self, item, quantity, user):
        shopping_list = self.get(user)
        shopping_list.delete(item, quantity)
        self._repository.save(shopping_list)
  
    def delete_all(self, user):
        self._repository.delete(user)

    def get(self, user) -> ShoppingList:
        result = self._repository.get(user)
        return result
    
    def reset(self, user):
        shopping_list = self.get(user)
        shopping_list.reset()
        self._repository.save(shopping_list)
