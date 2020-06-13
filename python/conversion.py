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



""" Number """

a = 123
a = str(a)
print(type(a)) # <class 'str'>

b = int(a)
print(type(b)) # <class 'int'>

k = divmod(10, 3)
#(3, 1) 10除以3等于3余1