#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self._title = None
        self._page_count = None
        
        self.title = title
        self.page_count = page_count

    def title(self):
        return self._title

    def title(self, value):
        self._title = value

    def page_count(self):
        return self._page_count

    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")