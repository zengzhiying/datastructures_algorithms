#!/usr/bin/env python3
# coding=utf-8
from shopping_cart import shopping

if __name__ == '__main__':
    items = [59, 23, 68, 99, 168, 321, 108, 11, 16, 27]
    condition = 200

    shop_items = shopping(items, condition)
    if shop_items:
        print(shop_items)

