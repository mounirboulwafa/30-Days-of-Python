items = ['item1', 'item2', 258.123, 1236, 'Mounir', 'Laptop', 1234]

str_item = []
num_item = []

for i in items:
    if isinstance(i, float) or isinstance(i, int):
        num_item.append(i)
    elif isinstance(i, str):
        str_item.append(i)
    else:
        pass

# Print the lists

print(items)
print(str_item)
print(num_item)


def parse_listes(some_list):
    str_list_item = []
    num_list_item = []
    for i in items:
        if isinstance(i, float) or isinstance(i, int):
            num_list_item.append(i)
        elif isinstance(i, str):
            str_list_item.append(i)
        else:
            pass

    return str_list_item, num_list_item


print(parse_listes(items))

items2 = ['item1', 'item2', [258.123, 1236, 2, 456, 0.55], 'Mounir', 'Laptop', 1234]

print(parse_listes(items2))


items3 = ['item1', 'item2', 258.123, 1236, 'Mounir', 'Laptop', 1234]
