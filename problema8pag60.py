A=set(input('introduceti elementele multimii A:'))
B=set(input('introduceti elementele multimii B:'))
a=0
for i in A:
    if ord(i) not in range(48,58):
        a+=1

for i in B:
   if ord(i) not in range(48,58):
        a+=1
if a>0:
    print('Multimile A si B trebuie sa fie formate din numere intregi')
if a==0:
  print('intersectia multimilor A si B:',A.intersection(B))
  print('reuniunea multimilor A si B:',A.union(B))
  print('diferenta multimilor A/B:',A.difference(B))
  print('diferenta multimilor B/A:',B.difference(A))