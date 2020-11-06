a = [1,2,3]
b = "abcdef tkh;lngk nmlh; g"

a[1] = 'y'
print(a)
print(a.pop(2))
print(a.append(0.33))
print(a)
x = b.split(';')
print(x)
delimiter = ' '
delimiter.join(x)
print(x)
#print(sorted(a*4))
a.extend(a)
#a.sort()
del a[3]
#a.remove('y')
print(a)
#open('')
