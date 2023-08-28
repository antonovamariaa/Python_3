# # ВАРИАНТ 1
# # можно использовать random для генерации количества ягод:

# import random
# n = int(input("enter bushes: "))
# list = []
# maxnum = 0

# for i in range (n):
#     list.append (random.randint(1,50))

# #print(list)

# for i in range(1,len(list)-1):
#     sumnum = list[i]+list[i+1]+list[i-1]
#     if (sumnum > maxnum):
#         maxnum = sumnum

# #последние два и первый
# new1 = list[n-1]+list[n-2]+list[0]
# #последний и два первых
# new2 = list[n-1]+list[0]+list[1]

# #проверка какая из комбинаций выше больше
# if new1 > new2:
#     newmax = new1
# else: 
#     newmax = new2

# if newmax > maxnum:
#     print(newmax)
# else:
#     print(maxnum)
#     newmax = 0



# # ВАРИАНТ 2
# #является немного измененным вариантом 2, где вместо random числа вводятся вручную:

n = int(input("enter bushes: "))
list = []
maxnum = 0

for i in range (n):
    list.append (int(input("enter berries: ")))

#print(list)

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

