from code_base_EP1 import *

## declaração das variáveis
P,Q,R,S = vars('P', 'Q', 'R', 'S')


affirming_the_consequent = ArgumentForm(
  P >> Q, Q,    #premises
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