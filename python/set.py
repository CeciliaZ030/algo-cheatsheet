
# https://realpython.com/python-sets/

''' initialization '''

y = set()
x = {'foo', 'bar', 'baz', 5.6, 9}

y.add(3)
y.add('a')
# {1, 'a'}
# add takes one arg at a time, can be int or str or tuple but cannot be list or dict

list(x)
# ['foo', 'bar', 'baz', 5.6, 9]
y.remove(3)

x.pop()
# removes and returns an arbitrarily chosen element from x. If x is empty, x.pop() raises an exception

x.clear()
# delete everthing

''' operation '''

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

x1 | x2
# {'baz', 'quux', 'qux', 'bar', 'foo'}

x1.union(x2)
# {'baz', 'quux', 'qux', 'bar', 'foo'}

x1 & x2
# {'baz'}
x1.intersection(x2)
# {'baz'}

 x1 - x2
 # {'foo', 'bar'}
 x1.difference(x2)
 # {'foo', 'bar'}

x1 ^ x2
# {'foo', 'qux', 'quux', 'bar'}
x1.symmetric_difference(x2)
# {'foo', 'qux', 'quux', 'bar'}

