""""""
"""
zip()
    - 将多个列表相同位置的元素归并到一个元组
"""

print("-------- zip举例 -------------")
l1 = [1, 2, 3]
l2 = [5, 6, 7]
z = zip(l1, l2)
print(z)
print(list(z))

z2 = zip(l2, l1)
print(list(z2))

# dict(zip()) 转换为字典格式
d = dict(zip(l1, l2))
print(d)
