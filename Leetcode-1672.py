accounts = [[2,8,7],[7,1,3],[1,9,5]]
maxi = 0
s = 0
for i in accounts:
    for j in i:
        s+=int(j)
    if s>maxi:
        maxi = s
    s = 0            
print(maxi)