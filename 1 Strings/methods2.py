# startswith() , endswith()

test = "hello world"

print(test.startswith('hello'))
print(test.startswith('world'))

print(test.endswith('world'))

print(test.startswith('h'))
print(test.endswith('d'))
print(test.startswith("w", 7 , 11))

print("-----------------------------------------")
#strip rstrip lstrip

test2 = '   HELLO , WORLD   '

print(test2.strip())
print(test2.rstrip())
print(test2.lstrip())


test3 = "@@@ Hello , World @@@"

print(test3)
print(test3.strip('@'))
print(test3.rstrip('@'))
print(test3.lstrip('@'))


test4 = "@#@#@# Hello , World @#@#@#"

print(test4)
print(test4.strip('@#'))
print(test4.rstrip('@#'))
print(test4.lstrip('#@'))

print("-----------------------------------------")
#zfill

hours = '1'
minutes = '9'
seconds = '36'
milseconds = '5'

print(f'hours : {hours}, minutes : {minutes}, seconds = {seconds}')

print(f'{hours}:{minutes}:{seconds}')
print(f'{hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}:{milseconds.zfill(3)}')

 


