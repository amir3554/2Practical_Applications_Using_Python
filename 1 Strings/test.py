# Hello how are you  --> you are how Hello

the_text = str(input("Enter a text and it will be fliped , make sure to put spaces between the words."))

the_list = the_text.split(' ')
the_2list = []
#reverse()يمكن ان تعكس عناصر القائمة
for i in range(len(the_list)+ 1):
    if i == 0: continue
    #    i = 1
    i *= -1
    the_2list.append(the_list[i])

print(' '.join(the_2list))
from functools import reduce
#the_main = reduce(lambda x, y:the_2list[x] + the_2list[y], the_2list)









