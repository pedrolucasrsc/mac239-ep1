from code_base_EP1 import *

## declaração das variáveis
P,Q,R,S = vars('P', 'Q', 'R', 'S')


affirming_the_consequent = ArgumentForm(
  P >> Q, Q ,    #premises
  conclusion = P
)

livro = ArgumentForm(
  P >> Q, Q >> R,
  conclusion = P >> R
)

modus_ponens = ArgumentForm(
  P, P >> Q,    #premises
  conclusion = Q
)

modus_tolens = ArgumentForm(
  P >> Q, ~Q,   #premises
  conclusion = ~P
)

#
disjunctive_syllogism = ArgumentForm(
  P | Q, ~P,    #premises
  conclusion = Q
)

#
hypothetical_syllogism = ArgumentForm(
  P >> Q, Q >> R,   #premises
  conclusion = R
)


non_sequitur = ArgumentForm(
  P,        #premises
  conclusion = Q
)


denying_the_antecedent = ArgumentForm(
  P >> Q, ~P,   #premises
  conclusion = ~Q
)

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

caso_com_árvore_não_binária = ArgumentForm(
  (R | R) | R ,
  conclusion = R
)
