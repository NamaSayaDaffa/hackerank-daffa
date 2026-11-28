
"""
insert i e  : Insert integer  at position .
print       : Print the list.
remove e    : Delete the first occurrence of integer .
append e    : Insert integer  at the end of the list.
sort        : Sort the list.
pop         : Pop the last element from the list.
reverse     : Reverse the list.
"""

n =  int(input())
lst = []
for i in range(n):
    cmd = list(input().split(" "))
    for j in range(len(cmd) - 1):
        cmd[j+1]  = int(cmd[j+1])
    if cmd[0] == "insert":
        lst.insert(cmd[1],cmd[2])
    elif cmd[0] == "print":
        print(lst)
    elif cmd[0] == "remove":
        lst.remove(cmd[1])
    elif cmd[0] == "append":
        lst.append(cmd[1])
    elif cmd[0] == "sort":
        lst.sort()
    elif cmd[0] == "pop":
        lst.pop()
    elif cmd[0] == "reverse":
        lst.reverse()
    
