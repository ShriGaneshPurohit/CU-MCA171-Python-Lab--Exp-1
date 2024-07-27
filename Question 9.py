A=['abc', 'xyz', 'aba', '1221']
lastItem = []

for itr in A :
        lastItem.append(itr[len(itr)-1])

print(lastItem)