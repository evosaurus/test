nrs=[2,1,3,2,1,2]
# gaat goed met "If the length of the list is even the middle element is defined to
# be the rightmost of the two elements in the middle of the list
print(len(nrs)//2)
print(nrs[len(nrs)//2])

nrs.sort(reverse=True)
###  nrs.reverse()
print(nrs)

nrs.sort()
# nrs.reverse()
print(nrs)
nrs.append(nrs.pop(0))
print(nrs)

