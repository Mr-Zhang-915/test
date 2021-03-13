name_list = ['Tom','Lily','Rose']
#1、index()
print(name_list.index('Tom'))               # 0
#print(name_list.index('Toms'))             #列表中不存在报错

#2、count()
print(name_list.count('Tom'))               # 1
#print(name_list.count('Toms'))             # 列表中不存在，返回0

# 3、len()
print(len(name_list))                       # 3