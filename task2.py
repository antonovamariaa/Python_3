import random
n = int(input("enter bushes: "))
list = []
maxnum = 0

for i in range (n):
    list.append (random.randint(1,50))

print(list)

for i in range(1,len(list)-1):
    sumnum = list[i]+list[i+1]+list[i-1]
    if (sumnum > maxnum):
        maxnum = sumnum

#последние два и первый
new1 = list[n-1]+list[n-2]+list[0]
#последний и два первых
new2 = list[n-1]+list[0]+list[1]

#проверка какая из комбинаций выше больше
if new1 > new2:
    newmax = new1
else: 
    newmax = new2


if newmax > maxnum:
    print(newmax)
else:
    print(maxnum)
    newmax = 0




