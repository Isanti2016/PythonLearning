
def fibonacci(max):
    n,a,b=0,1,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

g=fibonacci(10)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
