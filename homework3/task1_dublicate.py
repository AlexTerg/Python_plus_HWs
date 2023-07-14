lst = [1, 3, 5, 2, 1, 6, 1, 5, 8, 4]

new_lst = [i for i in lst if lst.count(i) > 1]
print(list(set(new_lst)))