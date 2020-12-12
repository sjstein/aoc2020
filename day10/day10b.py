"""

"""

def numhops(arr, dif):
    c = len(arr)-1
    hops = 0
    newarr = arr
    print(f'In numhops with array = {arr}')
    while c > 1:
        if (arr[c] - arr[c-2]) <= dif and (arr[c] > arr[c-1] > arr[c-2]):
            print(f'Found extra at {c-1} of value {arr[c-1]} ({arr[c-2]},{arr[c-1]},{arr[c]})')
            hops += 1
            #newarr.remove(newarr[c-1])
            #print(numhops(newarr, dif))
        c -= 1
    return hops

fname = 'temp.txt'
entries = []
with open(fname, 'r') as fp:
    for line in fp:
        entries.append(int(line.rstrip()))

entries.append(max(entries)+3)
entries.append(0)
entries.sort()

print(entries)
print(numhops(entries, 3))

