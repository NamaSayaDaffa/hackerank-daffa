n = int(input())
lst = []
for i in range(n):
    name = input()
    grade = float(input())
    lst.append([name, grade])
mini = min(lst, key=lambda x: x[1])
maks = max(lst, key=lambda x: x[1])
lst.sort(key=lambda x: x[0])
lst = list(filter(lambda x: x[1] > mini[1],lst))
mini = min(lst, key=lambda x: x[1])
lowest = [i[0] for i in lst if i[1] == mini[1]]
for i in lowest:
    print(i)

