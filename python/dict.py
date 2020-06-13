""" Dictionary """

d =  {'a': 1, 'b': 2}

# 加一对
d.update({'c': [3, 4], 'd': "hello"})
d.update({'a' : 0})
# 加key一样的会被替换掉


# iterate over dict
for key in d:
	print(key, d[key])

l_val = [v for v in d.values()]
l_key = [k for k in d.keys()]
l_items = [i for i in d.items()]
print(l_val, l_key, l_items)


d.keys()
# ['a', 'b', 'c']

d.values()
# [0, 2, [3, 4], "hello"]

print(d['a'])
# 0 -- 取value的时候直接用方括号拿key

print(d.items())
# dict_items([('a', 0), ('b', 2), ('c', [3, 4]), ('d', 'hello')])

d.__contains__('a')
# True

d.get('a')
# 0

d.pop('b')
# 2 -- 剩下 {'a': 0, 'c': [3, 4], 'd': 'hello'}

d.popitem()
# (('d', 'hello')) -- 剩下{'a': 0, 'c': [3, 4]}
 

d1 = {'a': [1, 2]}
d2 = d1
d2['a'] = [1, 2, 3, 4]
print(d1['a'])
# [1, 2, 3, 4] --别的reference会修改原本的dict

d2 = d1.copy()
# 这样就分开了

del d['a']
# 删除'a'

d.clear()
# 啥都没了

d.setdefault('third', '_')
print(d)
# {'third': '_'}

{}.fromkeys(['first', 'second'])
# {'first': None, 'second': None} 空dict的默认值为None



