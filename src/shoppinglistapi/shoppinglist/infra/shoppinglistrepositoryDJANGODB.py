from ..domain.shoppinglistrepository import ShoppingListRepository
from ..domain.shoppinglist import ShoppingList
from shoppinglistapi.models import ShoppingListDB, ShoppingListDetailDB
from django.db import transaction
import os
class ShoppingListRepositoryDJANGODB(ShoppingListRepository):
    def get(self, user) -> ShoppingList:
        result = ShoppingList(user)
        sl_table = ShoppingListDB.objects.filter(user_name = user).first()
        if(sl_table):
            sl_details = ShoppingListDetailDB.objects.filter(user_name = user)
            if(sl_details):
                for item in sl_details:
                    for i in range(0,item.item_quantity):
                        result.add(item.item_name)
        return result
            
    def save(self, shopping_list):
        with transaction.atomic():
            self._delete(shopping_list.get_user())
            sl_table = ShoppingListDB(user_name = shopping_list.get_user())
            sl_table.save()
            for index in range(0,shopping_list.size()):
                sl_detail = ShoppingListDetailDB(user_name = sl_table, 
                    item_name = shopping_list.get_item_description(index), 
                    item_quantity = int(shopping_list.get_item_quantity(index)))
                sl_detail.save()
    
    def delete(self, user):
        with transaction.atomic():
            self._delete(user)

    def _delete(self, user):
        sl_table = ShoppingListDB.objects.filter(user_name = user).first()
        if(sl_table):
            sl_table.delete()
