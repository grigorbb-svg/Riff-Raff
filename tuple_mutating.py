#Python ,  Am I mutating a tuple???
L=["list","of","things"]
T=("tuple","of","things",2,L)
print(T)
L.append('changed!')
L.pop(0);L.pop(0)
print(T)
