#!/usr/bin/env python3

import ipdb

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_item = []

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    for i in range(quantity):
        self.items.append(title)
    self.last_item = {"title": title, "price": price, "quantity": quantity}
    

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      discounted_total = self.total - (self.total * (self.discount * 0.01))
      self.total = int(discounted_total)
      print(f"After the discount, the total comes to ${self.total}.")

  def void_last_transaction(self):
    self.total -= self.last_item["price"] * self.last_item["quantity"]

  
