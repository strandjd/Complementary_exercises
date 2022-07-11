# a, b = 1, 2

# print(a, b)
# # 1 2

# print((a, b))
# #? (1 2)

# a, b = b, a
# print(a, b)
# #? 2 1

# a, b = b, a
# print(a, b)
# #? 1 2

# a, b, c = 1, 2, 3
# print(a, b, c)
# #? 1 2 3



# a, b, c = b, c, a
# print(a, b, c)
# #? 3 2 1



# a, b, c = b, c, a
# print(a, b, c)
# #? 2 1 3


# 2. 
# # do and explain the following:

# def dup():
#     return 1, 2
# a, b = dup()
# print(a, b)
# #? 1 2

# a = dup()
# print(a, b)
# #? 2.b





3. 
# iterator over a dictionary:
d = { 'a': 1, 'b': 2, 'y': 3 }
for key, value in d.items():
    print(key, value)
   
#? 3.a 'a': 1, 'b': 2, 'y': 3


for keyval in d.items():
    print(keyval)
   
#? 3.b 1, 2, 3


for keyval in d.items():
    print(keyval[0], keyval[1])
   
#? 3.c'a': 1, 'b': 2, 'y': 3


for keyval in d.items():
   key, val = keyval # lägger in keyval på variablerna key och val
   print(key, val)
   
#? 3.d