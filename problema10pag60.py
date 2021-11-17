X={1,2,3,4}
Y=[[]]
for x in X:
    Y+=[y + [x] for y in Y]
print(Y)