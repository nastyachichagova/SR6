
print ('Программа вычисляет количество элементов массива, отличающихся от минимального на DELTA')
try:
    a = [int(i) for i in input('Введите элементы массива через пробел: ').split()]
except:
    print ('Ошибка! Элементы массива должны быть целыми числами.')
    a = [0]
try:
    delta = int(input('Введите значение DELTA: '))
except:
    print ('Ошибка! DELTA должно быть целым числом.')
    delta = 0
    
k = l = 0

for i in a:
    l+=1

for i in range (l-1):
    for j in range (l-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

if l>1:
    for i in  range (l):
        if (a[i] == a[1] + delta) or (a[i] == a[1] - delta):
            k+=1
    print ('Ответ: ', k)
else:
    print ('Ответ: ', 0)
         
         

