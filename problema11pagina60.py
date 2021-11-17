X={'A','B','C','D'}
Y=[[]]
for x in X:
    Y+=[y + [x] for y in Y]
print(Y)