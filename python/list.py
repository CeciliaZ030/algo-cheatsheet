

""" Sting and char conversion """


# string to list

str1 = "Geeks for Geeks"
l1 = list(str1.split(" ")) 
print(l1)

# list to string 

str1 = " ".join(l1) # 如果双引号里是"," 那单词就会被","区别开
print(str1)


# word to list

str2 = "vocab"
l2 = list(str2)
print(l2)

# list to nested list

l3 = ["a, b, c", "d", "h, i", "123"]
nested_l3 = [elm.split(', ') for elm in l3]
print(nested_l3)


""" Iterations """

# iterate over string

str4 = "test"
for c in str4:
	print(c)


""" Methods """

# initializeing list with certian size
l = [None] * 10
l = [None for i in range(10)]

nested_l = [[None for i in range(5)] for j in range(10)]

stack = ['a','b']
stack.append('c')

stack.append(['d', 'e', 'f'])
print(stack)
# ['a', 'b', 'c', ['d', 'e', 'f']]

stack = ['a','b']
stack.extend(['d', 'e','f'])
print(stack)
# ['a', 'b', 'd', 'e', 'f']

my_list = ['a','b','c','b', 'a']
my_list.index('b')
# 1

my_list.index('b', 2)
# 3

my_list.insert(2, 'a')
# ['a','b', 'a', 'c', 'b', 'a']

my_list.remove('a')
# ['b', 'a', 'c', 'b', 'a']

my_list.count('b')
# 2

my_list.sort()
# ['a', 'a', 'b', 'b', 'c']

my_list.sort(reverse=True)
# ['c', 'b', 'b', 'a', 'a']


""" Operators """

my_list = [1]
my_list += [2]
my_list += [3, 4]
print(my_list)
# [1, 2, 3, 4]

my_list = my_list * 2
print(my_list)
# [1, 2, 3, 4, 1, 2, 3, 4]


""" Slicing """

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[1:7:2])
# [1, 3, 5] -- 从第一个到第七个，步长为2
#  list[first index:last index:step]

print(a[1:7])
# [1, 2, 3, 4, 5, 6] -- 步长默认为1

print(a[0::2])
# [0, 2, 4, 6, 8] -- index默认为最前或最后


""" List Comprehesnion """

evens = []
for i in range(10):
    if i % 2 == 0:
    	evens.append(i)

# 等同于
evens =  [i for i in range(10) if i % 2 == 0]
print(evens)
# [0, 2, 4, 6, 8]

test = [n/2 for n in evens if n > 5]
print(test)
# [3.0, 4.0] -- 6/2 和 8/2



""" 骚操作 """

cnt = collections.Counter([-1, 0, 1, 2, -1, -4])
print(cnt, cnt[-1])
# Counter({-1: 2, 0: 1, 1: 1, 2: 1, -4: 1}) 
# 1

# 把elm和index都列出来
nums = [1, 2, 3, 4, 1, 2, 3, 4]
nums = [[num,idx] for idx,num in enumerate(nums)]
print(nums)
# [[1, 0], [2, 1], [3, 2]....]
