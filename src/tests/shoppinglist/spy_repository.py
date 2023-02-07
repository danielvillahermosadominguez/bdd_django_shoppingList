from shoppinglistapi.shoppinglist.domain.shoppinglistrepository import ShoppingListRepository
from shoppinglistapi.shoppinglist.domain.shoppinglist import ShoppingList

class ShoppingListRepositorySpy(ShoppingListRepository):

    def __init__(self):
        self._dictionary = {}

    def get(self, user) -> ShoppingList:
        if user in self._dictionary.keys():
            result = self._dictionary[user]
        else:
            result = ShoppingList(user)
            self._dictionary[user] = result
        
        return result

    def save(self, shopping_list):
        self._dictionary[shopping_list.get_user()] = shopping_list

    def delete(self, user):
        self._dictionary.pop(user)
        print("hola")
    
    def get_dic(self) -> dict:
        return self._dictionary;

