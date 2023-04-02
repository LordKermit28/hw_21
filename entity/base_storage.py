from entity.abstact_stotage import AbstractStorage
from exceptions import NotEnoughSpace, NotEnoughProduct, UnknownProduct



class BaseStorage(AbstractStorage):

    def __init__(self, items, capacity):
        self.__items = items
        self.__capacity = capacity

    def add(self, name, amount):
        if self.get_free_space() < amount:
            raise NotEnoughSpace

        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def remove(self, name, amount):
        if name not in self.__items:
            raise UnknownProduct

        if self.__items[name] < amount:
            raise NotEnoughProduct

    def get_free_space(self):
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)


