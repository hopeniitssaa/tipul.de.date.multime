X= set(map(str, input('introduceti primul sir de caractere: ').split()))
Y= set(map(str, input('introduceti al doilea sir de caractere: ').split()))
print('a) Caracterele care se intalnesc cel putin in unul dintre siruri: ', sorted(X.union(Y)))
print('b) Caracterele care apar in ambele siruri: ', sorted(X.intersection(Y)))
print('c) Caracterele care apar in primul si nu apar in sirul al doilea: ', sorted(X.difference(Y)))