# upper()
#هذه الدوال ان تعدل على السلسة النصية لانها غير قابلية لالتعديل لكنها تعيد سلسلة نصية جديدة
#str1 = str1.upper()من اجل التعديل

str1 = "Hello amir"

print(str1.upper())

print("---------------------------------------")

# lower

str2 = 'Hello, saleh'

print(str2.lower())

print("---------------------------------------")

feeling = input("how are you.")
if feeling.lower() == 'great':
    print("Me too!")

else:
    print("I hope you're ok")

print("---------------------------------------")

# isupper  , islower

str3 = "Hello amir"
print(str3.islower())
str3 = "hello amir"
print(str3.islower())

str4 = "Greetings amir"
print(str4.isupper())

str4 = "GREETINGS AMIR"
print(str4.isupper())

print("---------------------------------------")

# title تحويل السلسلة النصية الى عنوان و يكون الحرف الاول لكل كلمة الى حرف كبير

str5 = "Welcome to my 2nd world ."

print(str5.title())


print("---------------------------------------")

#capitalize تحويل اول حرف في الجمة فقت الى حرف كبير و باقي الاحرف الى صغيرة

str6 = "welcome To my 2nd World"

print(str6.capitalize())


print("---------------------------------------")

# swapcase يبدل الاحرف الصغيرة باحرف كبيرة

str7 = "Hello my name is DAWOOD"

print(str7.swapcase())

