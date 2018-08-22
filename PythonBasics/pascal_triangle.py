

def pascal_triangle(line):
    i,arr=0,[1]
    for i in range(line):
        yield arr
        arr=[1]+[arr[i]+arr[i+1] for i in range(0,len(arr)-1)]+[1]
    return 'over'

g=pascal_triangle(10)
while True:
    try:
        x=next(g)
        print(x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
