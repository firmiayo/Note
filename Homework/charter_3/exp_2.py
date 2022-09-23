from math import sqrt

from random import randint

exa=list()
couts=list(range(1,4))
for cout in couts:
    n=int(randint(0,100))
    exa.append(n)
print(f"No sorted :{exa}")
print(f"After sorted :{sorted(exa)}")