A=set(input('introduceti elemnetele multimii A:').split())
litere=True
for a in A:
    if ((ord(a)<65)or(ord(a)>90)):
        litere=False
if litere==True:
    B=set(input('introduceti elemnetele multimii B: ').split())
    litere2=True
    for b in B:
        if ((ord(b)<65)or(ord(b)>90)):
            litere2=False
    if litere2==True:
        print('a)intersectia multimilor:',A.intersection(B))
        print('b)reuniunea multimilor:',A.union(B))
        print('c)diferenta multimilor A/B:',A.difference(B))
        print('d)intersectia multimilor B/A:',B.difference(A))
    else:
        print("doar literele mari ale alfabetului latin")
else:
    print("doar literele mari ale alfabetului latin")