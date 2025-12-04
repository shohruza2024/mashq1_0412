#1-misol
roy = [12, 45, 67, 23, 89, 56]
print(roy)

natija = list(filter(lambda x: x % 3 == 0 and x > 5, roy))
print(natija)

#2-misol
roy = ['aziza', 'bob', 'tom', 'tamat', 'uzum']
print(roy)

natija = list(filter(lambda x: x[0] == x[-1], roy))
print(natija)

#3-misol 
soz = ['aziza', 'bob', 'tom', 'tamat', 'uzum']
n = int(input('unlikni bilish un raqam kirit: '))

natija = list(filter(lambda x: len(x) == n, soz))
print(natija)

#4-misol
roy = ['Anna', 'bob', 'Alex', 'tom', 'Jack']
print(roy)

natija = list(filter(lambda x: x[0] == x.title(), roy))
print(natija)

#5-misol
roy = [12, 45, 78, 35, 67]
print(roy)

natija = list(filter(lambda x: x % 2 != 0 and x > 0, roy))
print(natija)

