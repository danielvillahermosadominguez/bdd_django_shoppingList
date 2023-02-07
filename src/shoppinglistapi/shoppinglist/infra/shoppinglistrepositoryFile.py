from ..domain.shoppinglistrepository import ShoppingListRepository
from ..domain.shoppinglist import ShoppingList
import os
import json
from types import SimpleNamespace


class ShoppingListRepositoryFile(ShoppingListRepository):
    _FOLDER = "./data/"
    _FILE_EXTENSION = ".json"

    def get(self, user) -> ShoppingList:
        file_name = self._fileNameFromUser(user)
        if(not self._existFile(file_name)):
            return ShoppingList(user)

        return self.get_from_file(file_name)

    def save(self, shopping_list):
        if(not self._existFolder(self._FOLDER)):
            os.mkdir(self._FOLDER)

        file_name = self._fileNameFromShoppingList(shopping_list)
        content = self._convertToJSON(shopping_list)
        self._save_in_file(file_name, content)
    
    def delete(self, user):
        file_name = self._fileNameFromUser(user)
        if(self._existFile(file_name)):
            os.remove(file_name)   

    def _existFile(self, file_name):
        return os.path.isfile(file_name)

    def _existFolder(self, folder):
        return os.path.isdir(folder)

    def get_from_file(self, file_name) -> ShoppingList:
        with open(file_name, "r") as file:
            content = file.read()
            json_dic = json.loads(content)
            result = ShoppingList(json_dic['_user'],json_dic['_dict'])
        return result

    def _save_in_file(self, file_name, content):
        with open(file_name, "w+") as file:
            file.write(content)

    def _fileNameFromShoppingList(self, shopping_list):
        user = shopping_list.get_user()
        file_name = self._fileNameFromUser(user)
        return file_name

    def _fileNameFromUser(self, user):
        return self._FOLDER + user + self._FILE_EXTENSION

    def _convertToJSON(self, shopping_list):
        return json.dumps(shopping_list.__dict__)
