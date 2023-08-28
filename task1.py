
n = int(input("enter n: "))
m = int(input("enter m: "))
check = 0

list1n = []
list2m = []
list_result = []

print("fill list 1:")
for i in range (n):
    list1n.append (int(input("enter number: ")))

print("fill list 2:")
for i in range (m):
    list2m.append(int(input("enter number: ")))

list1n = set(list1n)
list2m = set(list2m)

for i in list2m:
    if i in list1n:
        list_result.append(i)

list_result.sort
print(list_result)


