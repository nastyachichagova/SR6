
array = [int(i) for i in input('Введите элементы массива через пробел: ').split()]
delta = int(input('Введите значение DELTA: '))
k = 0
for i in range (len(array)):
         if (array[i] > delta):
             k+=1
print (k)
         
         

