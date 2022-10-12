from collections import Counter,deque,OrderedDict

s= "00001105"
n= len(s)
_counter= Counter([int(x) for x in s])
_sortedCounter= sorted(_counter.items(), key=lambda x: x[0],reverse=True)
print(_sortedCounter)
ans=deque()
for i in range(len(_sortedCounter)):
    if(_sortedCounter[i][1] % 2 == 0):
        ans.append(_sortedCounter[i])
for i in range(len(_sortedCounter)):
    if(_sortedCounter[i][1] % 2 == 1):
        ans.append(_sortedCounter[i])
        break
print(ans)
s2=""
for i in ans:
    print(i)
    s2+= (str(i[0]) * (i[1]//2))
s2= s2 + (str(ans[-1][0]) * (ans[-1][1])) + s2[::-1]
s2= s2.strip("0")
print(s2)
