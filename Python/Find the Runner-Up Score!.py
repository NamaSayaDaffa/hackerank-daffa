n = int(input())
lst = list(map(int, input().split()))
maks = max(lst)
while maks in lst:
    lst.remove(maks)
print(max(lst))
