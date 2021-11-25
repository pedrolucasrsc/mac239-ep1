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



def trim (a, s):
  """"Recebe uma lista e retorna a lista aparada tal que seu novo tamanho seja s"""
  while(len(a) > s):
    a.pop()


def size_up_betas(ramo, betas, lo):
  for j in range(lo,len(ramo)):
    if ramo[j].alfaorbeta() == "beta":
      betas.append(True)
    else:
      betas.append(False)


def expansãoalfa(ramo, betas, lo):
  i = lo
  a = len(ramo)
  while(i < len(ramo)):
    if len(ramo[i].children) == 0:     #  É um átomo
      i += 1
      continue
    if ramo[i].alfaorbeta() == "alfa":
      ramo[i].alfaexp(ramo)
      #betas.append(False)
    #else:
      #betas.append(True)
    i += 1
  size_up_betas(ramo, betas, a)


printou_contra = False

def expande(ramo, betas, lo, hi):
    global printou_contra
    #print("INICIO")
    #show(ramo)
    #print(betas)
    if((not check(ramo)) or (printou_contra)):
      return
    expansãoalfa(ramo,betas,lo)       # Checa se tem expansão alfa e, se tiver, já faz.
    lo = len(ramo)-1                  # atualiza o lo
    #print("DEPOIS DO EXPALF")
    #show(ramo)
    #print(betas)
    #input()
    i = beta_search(betas)
    if(i != -1):            # ache um beta X no array de betas
        betas[i] = False              # se achou, marca esse beta e expande seus filhos
        b1, b2 = ramo[i].betaexp()
        ramo.append(b1)
        size_up_betas(ramo, betas, lo+1)
        hi = len(ramo)-1              # atualiza o hi 
        #show(ramo)
        #print(betas)
        #input()                
        expande(ramo, betas, lo, hi)                  
        trim(ramo, hi)                # Vamos dar pop até a posição que estamos, (hi)
        trim(betas, hi)      
        ramo.append(b2)
        size_up_betas(ramo, betas, lo)
        expande(ramo, betas, lo, hi)
    else:                             # Se chegou aqui, não tem mais oquê expandir.
      if(check(ramo)):
        print("Contra exemplo:")      # Vamos mostrar o ramo coerente
        show(ramo)  
        printou_contra = True

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

opa = ArgumentForm(
  premissa1, premissa2,
  conclusion = conc1
)
teste1 = ArgumentForm(
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

# invalid argument forms
non_sequitur = ArgumentForm(
  P,        #premises
  conclusion = Q
)

#################################################### resolvendo ########################## 

for d in teste1.premises:
  d.mark('T')
  ramo.append(d)

teste1.conclusion.mark('F')
ramo.append(teste1.conclusion)

ramo1 = deepcopy(ramo)

betas = []

size_up_betas(ramo1, betas, 0)

expande(ramo1, betas, 0, len(ramo)-1)
if(not printou_contra):
  print("VERDADEIRO")



