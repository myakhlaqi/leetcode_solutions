# [0,0,1,0,1,1,1,0,1,1]
# output :3

A= [0,0,1,0,1,1,1,0,1,1]
n= len(A)
max_con=0
count=0
for i in A:
    if(i == 1):
        count +=1
    else:
        if(count> max_con):
            max_con= count
        count = 0
print(max_con)
