from itertools import count
from os import remove

# soru a
original_List = ['There', 'is','a','little','dog','in','the','University','.','The','little','cat','saw', 'the',
                 'dog','in','the','University','.']
stop_w =['a','an','.','The','the']


for i in range(len(stop_w)):
    while stop_w[i] in original_List:
        original_List.remove(stop_w[i])
print(original_List)

# soru b
a_dict = dict()

for i in range(len(original_List)):
    single_word = original_List[i]
    amount_of_words = original_List.count(single_word)
    a_dict[single_word] = amount_of_words # dict'e  nasıl ekleme yapılacağını chatGpt'den öğrendim
print(a_dict)

# soru c
new_list = set()
for i in range(len(original_List)):
    single_word = original_List[i]
    new_list.add(single_word)      # set'e ekleme yapmak için add kullanılacağını chatGpt'den öğrendim
new_list = list(new_list)
print(new_list)

# dördüncü ??









 #   original_List.pop(stop_w,stop_w[i])


