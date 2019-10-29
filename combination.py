def insert(list1, num, row):
    list1[row%num:row%num] = [num]

num = int(input('input n: '))
list1 =[]
numFactorial = 1
i = 1
while i < num:
    i += 1
    numFactorial *= i

list1[0:0] = [[]* it for it in range(numFactorial)]

for itt in range(1, num+1):
    for it in range(numFactorial):
        insert(list1[it], itt, it)    
    list1.sort()

# print(list1)
for it in range(numFactorial):
    print(list1[it])
