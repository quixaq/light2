def toBinary(n):
    if isinstance(n,str):
        if n.isdigit():
            n=int(n)
        else:
            return "ERR: Arg isn't a digit"
    elif not isinstance(n,int):
        return "ERR: Arg can only be string either int"
    b=[1]
    p=1
    while b[-1]*2<=n:
        b.append(2**p)
        p=p+1
    i=1
    r=""
    while i<=len(b):
        if b[-i]<=n:
            n=n-b[-i]
            r="1"+r
        else:
            r="0"+r
        i=i+1
    return int(r[::-1])
def fromBinary(n):
    if isinstance(n,int):
        n=str(n)
    elif isinstance(n,str):
        if not n.isdigit:
            return "ERR: Arg isn't a digit"
    else:
        return "ERR: Arg needs to be int either string(digit)"
    i=len(n)
    b=[1]
    t=1
    while t<i:
        b.append(2**t)
        t+=1
    t=0
    r=0
    while t<i:
        if n[t]=="1":
            d=t+1
            r=r+b[-d]
        t=t+1
    return r
    