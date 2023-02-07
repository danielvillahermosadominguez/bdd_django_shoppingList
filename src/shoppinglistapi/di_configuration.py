import pinject
from shoppinglistapi.shoppinglist.infra.shoppinglistrepositoryFile  import ShoppingListRepositoryFile
from shoppinglistapi.shoppinglist.infra.shoppinglistrepositoryDJANGODB import ShoppingListRepositoryDJANGODB

class BindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('repository', to_instance = ShoppingListRepositoryFile())