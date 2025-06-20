import re

# isdecimal()

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email = "example@test.com"
if re.match(pattern, email):
    print("البريد الإلكتروني صحيح")
else:

    print("البريد الإلكتروني غير صحيح")


print('--------------------------------------------------')


text = "الرقم الأول هو 123 والرقم الثاني هو 456."
pattern = r"\d+"
numbers = re.findall(pattern, text)
print(numbers)  # ['123', '456']


print('--------------------------------------------------')


text = "أنا أحب البرمجة بلغة بايثون."
pattern = r"بايثون"
new_text = re.sub(pattern, "جافا", text)
print(new_text)  # "أنا أحب البرمجة بلغة جافا."


print('--------------------------------------------------')


is_phone_number = r'\d{3}-\d{3}-\d{4}'
my_phone = '123-456-7890'

if re.match(is_phone_number, my_phone):
    print('Your good to go.')
else:
    print("invalid phone number.")


print('--------------------------------------------------')


rr = r'name\sis\s\w{0,10}'

info = '''hello my name is Amoor , my phone number is 123-456-7890.
and her name is mariam and her phone number is 098-765-4321'''

the_resault = re.findall(rr, info)

print(the_resault)


print('--------------------------------------------------')


info2 = '''123-455-9999

*123-555-8888

321 455 9999

*321 455 9999

111 222 7777****'''

rr2 = r'\d{3}-?\s?\d{3}-?\s?\d{4}'

print(re.findall(rr2, info2))


print('--------------------------------------------------')

def phonechecker():
    inter_the_phone = input('please inter your phone number.')
    inter_the_phone = str(inter_the_phone)
    phones = []

    def check_phone_number(the_phone):
            true_phone = re.findall(rr2, the_phone)
            if true_phone:
                for phone in true_phone:
                    phones.append(phone)
            else:
                print('Invalid phone number.')

    check_phone_number(inter_the_phone)
    print(phones)


print('--------------------------------------------------')


# search

text3 = '''hello im amir and my number is 123 456 2552
and she is mariam and her phone number is 321 654 5225'''

resault2 = re.search(r'\d{3}-?\s?\d{3}-?\s?\d{4}', text3)

print(resault2)
print(resault2.group())
print(resault2.string)


print('--------------------------------------------------')


# sub()


text4 = '''hello im amir and my number is 123 456 2552
and she is mariam and her phone number is 321 654 5225'''

replace = re.sub(r'\d{3}-?\s?\d{3}-?\s?\d{4}', '123-456-2552', text4, 1)
print(replace)



print('--------------------------------------------------')


text5 = 'Hello im Amir writing a program.'

replace2 = re.sub(r'\s', '_', text5)

print(replace2)


print('--------------------------------------------------')


# split

text5 = 'Hello im Amir writing a program.'

resault3 = re.split(r'\s', text5)

print(resault3)

resault3 = re.split(r'\s', text5, 3)

text6 = 'استبدال-وتقطيع-النصوص-عبر-دوال-الوحدة'

replace4 = re.sub(r'-', ' ', text6)

print(replace4)


print('--------------------------------------------------')


# groups

number = '123-444-5555'

resault5 = re.search(r'(\d{3})-(\d{3}-\d{4})', number)

print(resault5.group())
print(resault5.group(0))
print(resault5.group(1))
print(resault5.group(2))


print('--------------------------------------------------')

date = '27-05-2021'

resault6 = re.search(r'(\d{2})-(\d{2})-(\d{4})', date)

#day = resault6.group(1)
#month = resault6.group(2)
#year = resault6.group(3)

day, month, year = resault6.groups()

print(f'The day is {day}, the month is {month}, the year is {year}.')


print('--------------------------------------------------')

rr3 = r'[a-zA-Z0-9%&._@!+=-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}'

emails ='''
amir.dikat@gmail.com
hasouba_cademy@gmail.net
HASOUBACADEMY@gmail.edu
HasoubAcademy321@yahoo.com
hsb-ac.demy13544t52@gmail.net
amirii@hotmail.com
'''
checked_emails = re.findall(rr3, emails)
print(checked_emails)

#checked_emails = []
#search = re.search(rr3, emails)
#for email in range(5):
#    checked_emails.append(search.group(email))
#print(checked_emails)

