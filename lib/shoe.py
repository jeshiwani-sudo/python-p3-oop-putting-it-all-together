#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = None
        self._size = None  

        self.brand = brand
        self.size = size

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")
            if not hasattr(self, '_size'):
                self._size = None

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
