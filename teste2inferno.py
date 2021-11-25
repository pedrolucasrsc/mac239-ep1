#import code_base as CB
from collections import deque

from code_base_EP1 import *

from copy import deepcopy

def all_atoms(a, tam):
    for i in range(tam, len(a)):
        if(not a[i].isatom()):
            return False
    return True  

def beta_search(a):
    for i in range(len(a)-1, -1, -1):
        if a[i]:
            return i
    else:
        return -1
        
        


def expande(ramo, betas, lo, hi):
    se há contradição: retorne
    se não dá pra expandir: temos que dar o contra exemplo ## não precisa checar se tem contradição
    
    temos que expandir
    
    se tem expansão alfa (olhamos a partir da posição lo, até o final da lista.):
        expande todos os alfas
        atualiza o lo
    i = beta_search(betas)
    if(beta_search != -1):
        b1, b2 = ramo[i].beta_exp()
        ramo.append(b1)
                                               ## ache um beta X no array de betas
        expande()                  ## vamos expandir esse beta.
        ramo.pop()   ## Vamos dar pop até a posição que estamos, (hi)      ## se achou, marca esse beta e expande seus filhos
        ramo.append(b2)
        expande()
                                  



def show(a):
  for i in a:
    print(f"({i.marking}){i}", end = "  ")
  print()
        
def check(ramo):
  """ 
    It returns True if the branch isn't closed, otherwise, it returns False

  """
  truths = []
  falses = []
  for elem in ramo:
    if elem.is_atom():
      if elem.marking == "T":
        if elem in falses:
          return False
        else:
          truths.append(elem)
      else:
        if elem in truths:
          return False
        else:
          falses.append(elem)
  return True



def expansãoalfa(a, b,tam):
  for i in range(tam,len(a)):
    if len(a[i].children) == 0:
      continue
    if a[i].alfaorbeta() == "alfa":
      a[i].alfaexp(a)
      b.append(False)
    else:
      b.append(True)
  show(a)
  print(check(ramo))
  print(b)
    



def copy_preposition(preposition):
  return deepcopy(preposition)
# fórmulas
# todos os átomos que serão utilizados nas fórmulas precisam ser declarados
P,Q,R,S = vars('P', 'Q', 'R', 'S')

#declaracao da formula
premissa1 = P >> Q
premissa2 = Q >> R
conc1 = P >> R

ramo = []
pilhaderamos = deque()

teste1 = ArgumentForm(
  premissa1, premissa2,
  conclusion = conc1
)

#################################################### resolvendo ########################## 

for d in teste1.premises:
  d.mark('T')
  ramo.append(d)

teste1.conclusion.mark('F')
ramo.append(teste1.conclusion)

tam1 = len(ramo)
tam2 = tam1 + tam1*2

ramo1 = deepcopy(ramo)

betas = []


tamatual = len(ramo1)

for e in ramo1:
  if len(e.children) == 0:
     continue
  if e.alfaorbeta() == "alfa":
    e.alfaexp(ramo1)
    betas.append(False)
  else:
    betas.append(True)
show(ramo1)
print(check(ramo))
print(betas)

tam_atual = 0

while(check(ramo1) or len(pilhaderamos) > 0):
  expansãoalfa(ramo1, betas, tam_atual)
  tam_atual = len(ramo1)
  for i in range(len(betas)-1, -1, -1):
    if(betas[i]):
      b1, b2 = ramo1[i].betaexp()
      betas[i] = False
      pilhaderamos.append([b2, betas, tam_atual])
      ramo1.append(b1)
      


      

  # expande beta1
  # ramo = ramo que foi expandido com beta1
  # empilha beta2
  if (not check(ramo1)):
    ramo1 = pilhaderamos.pop()
  # ramo = pilha.pop()



