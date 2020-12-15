#usr/bin/env/python3
#yang not
print('======NOT======')
a = True
c = not a
print('data a = ' ,a)
print('data c = ' ,c)
#yang or
print('======OR========')
# True & False
a = True
b = False
c = a or b
print(a,'OR' ,b, '=' ,c) 
#True & True
a = True
b = True
c = a or b
print(a,'OR' ,b, '=' ,c) 
#False & True
a = False
b = True
c = a or b
print(a,'OR' ,b, '=' ,c) 
#False & False
a = False
b = False
c = a or b
print(a,'OR' ,b, '=' ,c)
#yang AND
print('======AND========')
# True & False
a = True
b = False
c = a and b
print(a,'AND' ,b, '=' ,c) 
#True & True
a = True
b = True
c = a and b
print(a,'AND' ,b, '=' ,c) 
#False & True
a = False
b = True
c = a and b
print(a,'AND' ,b, '=' ,c) 
#False & False
a = False
b = False
c = a and b
print(a,'AND' ,b, '=' ,c)

