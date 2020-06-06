i = 0

while i < 10:
  i += 1


for j in "hello world":
   if j == "o":
        del()
   elif j == "l":
       continue
   elif j == "r":
       break
   else:
       print(j, end = '')

l = []
b = [24,67]
lis = [1,56,'x',34,2.34,['s','t','r','o','k','a']]

a = [a + b
     for a in 'list'
     if a != 's'
     for b in 'soup'
     if b != 'u']

l.append(23) #- добавление к концу
l.append(34) #- добавление к концу
l.append(34) #- добавление к концу
l.extend(b)  #-добавление
l.insert(1, 56) #- замена
l.remove(34)
l.pop(0)
l.index(56) #- узнаём его индекс
l.count(34) #- кол-во элементов в списке
l.sort() # - сортировка от меньшего ск большему
l.reverse() #- переворачивает список, наоборот
l.clear()  # - очищает весь список

l1 = [34,'sd',56,34.34]
print(l[0])

# ITEM[START:STOP:STEP]  - начали, когда заканчивать и шаги

# Картеж - массив который нельзя изменять ( они весят меньше)

a2 = (43,56,45.23) # - кортеж пишется черещ ()

a = tuple("hello world") # - разделяет на элементы h e l l o w o r l d 