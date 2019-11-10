"""
Task:
You are the manager of a supermarket. You have a list of N items together with their prices that consumers bought on a
particular day. Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format:
The first line contains the number of items, N.
The next N lines contains the item's name and price, separated by a space.

Output Format:
Print the item_name and net_price in order of its first occurrence.
"""

from collections import OrderedDict

N = int(input())

purchased_items = OrderedDict()
for i in range(N):
    item_name = ' '
    info = input().split()
    net_price = int(info[-1])
    words = info[0:-1]
    item_name = item_name.join(words)
    if item_name in purchased_items:
        new_price = purchased_items[item_name] + net_price
        purchased_items[item_name] = new_price
    else:
        purchased_items[item_name] = net_price

for item in purchased_items:
    print(item, purchased_items[item])
