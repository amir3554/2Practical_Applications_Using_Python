#index(substring, start , end)
test = 'Hello Amir'
print(test.index('Amir'))
print(test.index('A'))

try:
    print(test.index('Amir', 0, 5))
except ValueError:
    print("It seems like its not here.")

print("--------------------------------------")

#find(substring, start, end)
#تعمل نثل اندكس ولاكن بدون اظهار خضأ فاليو ارور , فقط تظهر -1
test2 = 'Hello Amir'
print(test2.find('Amir'))
print(test2.find('A'))


print("--------------------------------------")

#replace(old value, new value, count)
text1 = 'one plus one equal two'

print(text1.replace("one", "1"))
print(text1.replace("one", "1", 1))









