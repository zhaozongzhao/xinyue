h=[]
def toUppers(L):
    for x in L:
        if isinstance(x,str):
          h.append(x.upper())
    return h

print (toUppers(['Hello', 'world', 101]))