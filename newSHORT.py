
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""  
for i in list1:
    print(i) 
# вывод всего

for i in list1:
    if i%2 == 0:
        print(i)
    else:
        print("НЕ четное!")
#если что-то
"""
#кратко
new_list1 = [i for i in list1 if i%2==0]
new_list2 = [i*2 for i in list1] #умножаем на 2
print(new_list1)