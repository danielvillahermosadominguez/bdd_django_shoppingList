class ItemNotFoundError(Exception):
    def __init__(self, item):
        self.message = "There is not an item called " + item
        super().__init__(self.message)