from code_base_EP1 import *

## ~ NOT
## & AND
## | OR
## >> IMPLICA
## 

## declaração das variáveis
P,Q,R,S = vars('P', 'Q', 'R', 'S')

a = ArgumentForm(
  ~P >> Q,    #premises
  conclusion = ((~P >> ~Q) >> P)
)
b = ArgumentForm(
  P >> Q, ~Q,    #premises
  conclusion = ~P
)
c = ArgumentForm(
  ~Q >> ~P,    #premises
  conclusion = P >> Q
)
d = ArgumentForm(
  ~(P | Q),    #premises
  conclusion = ~P & ~Q
)
e = ArgumentForm(
  ~P & ~Q,    #premises
  conclusion = ~(P | Q)
)
f = ArgumentForm(
  ~(P & Q),   #premises
  conclusion = ~P | ~Q
)
g = ArgumentForm(
  ~P | ~Q,    #premises
  conclusion = ~(P & Q)
)
h = ArgumentForm(
  P | (Q & R) ,    #premises
  conclusion = (P | Q) & (P | R) 
)
i = ArgumentForm(
  (P | Q) & (P | R),    #premises
  conclusion = P | (Q & R)
)
j = ArgumentForm(
  P & (Q | R),    #premises
  conclusion = (P & R) | (P & R)
)
k = ArgumentForm(
  (P & Q) | (P & R),    #premises
  conclusion = P & (Q|R)
)

## ~ NOT
## & AND
## | OR
## >> IMPLICA
## 