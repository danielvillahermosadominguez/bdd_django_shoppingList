from shoppinglistapi.shoppinglist.domain.shopping_list_errors import ItemNotFoundError


class ShoppingList:
    def __init__(self, _user, _dict=None):
        self._user = _user
        if(_dict is None):
            self._dict = {}
        else:
            self._dict = _dict

    def get_user(self) -> str:
        return self._user

    def add(self, item):
        quantity = 0
        if(item in self._dict):
            quantity = self._dict[item]
        self._dict[item] = quantity + 1

    def reset(self):
        for key in self._dict.keys():
            self._dict[key] = 1
    
    def delete(self, item, quantity):
        if(not item in self._dict):
            raise ItemNotFoundError(item)

        new_quantity = self._dict[item] - quantity
        self._assing_quantity(item, new_quantity)

    def change(self, olditem, newitem):
        if(not olditem in self._dict):
            raise ItemNotFoundError(olditem)
        result = self._dict[olditem]
        if(newitem in self._dict):
            result = result + self._dict[newitem]
        self._dict[newitem] = result
        self._dict.pop(olditem)
        
    def delete_all(self):
        self._dict.clear()

    def size(self) -> int:
        return len(self._dict)

    def get_item_description(self, index) -> str:
        keys = list(self._dict.keys())
        return keys[index]

    def get_item_quantity(self, index) -> str:
        values = list(self._dict.values())
        return values[index]

    def _assing_quantity(self, item, quantity):
        if(quantity > 0):
            self._dict[item] = quantity
        else:
            self._dict.pop(item)
