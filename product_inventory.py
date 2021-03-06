#!/usr/bin/python
# Author:	@BlankGodd

class Product:

    __id = 0

    def __init__(self, name, price, quantity):
        Product.__id += 1
        self.price = price
        self.id = Product.__id
        self.quantity = quantity
        self.name = name

    def add_quantity(self, quantity):
        self.quantity += quantity

    def remove_quantity(self, quantity):
        self.quantity -= quantity

    def change_price(self, price):
        self.price = price

    def __str__(self):
        return "ID: {0}\tName: {1}\tPrice: {2}\tQuantity: {3}\
        ".format(self.id, self.name, self.price, self.quantity)


class Inventory:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def add_products(self, products):
        for i in products:
            self.products.append(i)

    def remove_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                break

    def show(self):
        print('-' * 63)
        for product in self.products:
            print(product)
        print('-' * 63)

    def edit_products(self):
        return self.products


