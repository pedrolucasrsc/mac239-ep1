from collections import deque
from code_base_EP1 import *
from copy import deepcopy
from argumentos import *

def imprime(resultado, tipo, formula):
  print(f"Resultado: ({resultado.marking}){resultado}     Tipo: {tipo:^4}      Fórmula de Origem: ({formula.marking}){formula}     ")
  print()



def beta_search(a): 
  """ Encontra a primeira Preposição beta que ainda não foi aberta da direita pra esquerda """
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
  """ Retorna True se o ramo estiver aberto e False se estiver fechado """
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

def trim(a, len_que_queremos):
  """" Recebe uma lista e retorna a lista aparada tal que seu novo tamanho seja s """
  while(len(a) > len_que_queremos):
    a.pop()

def size_up_betas(ramo, betas, lo):
  """ Atualiza lista de betas em um ramo """
  for j in range(lo,len(ramo)):
    if ramo[j].alfaorbeta() == "beta":
      betas.append(True)
    else:
      betas.append(False)

def expansãoalfa(ramo, betas, lo):
  """ Realiza todas as expansões alfa ainda presentes em um ramo """
  i = lo
  a = len(ramo)
  while(i < len(ramo)):
    if len(ramo[i].children) == 0:     #  É um átomo
      i += 1
      continue
    if ramo[i].alfaorbeta() == "alfa":
      resultado = ramo[i].alfaexp()
      if type(resultado) == list:
        ramo.extend(resultado)
        for elem in resultado:
          imprime(elem, "α", ramo[i])
      else:
        ramo.append(resultado)
        imprime(resultado, "α", ramo[i])
    i += 1
    
  size_up_betas(ramo, betas, a)

### Booleano global que olha se já foi encontrado algum ramo saturado e aberto
printou_contra = False

def expande(ramo, betas, lo):
  """ Executa as expansões alfa e beta ainda presentes no ramo """
  
  global printou_contra
  if((not check(ramo)) or (printou_contra)):
    return
  expansãoalfa(ramo,betas,lo)      # Checa se tem expansão alfa e, se tiver, já faz.
  if(not check(ramo)):  return      
  lo = len(ramo)-1                  # Atualiza o lo
  i = beta_search(betas)            # Acha um beta X no array de betas
  if(i != -1):                       
    betas[i] = False                # Se achou, marca esse beta e expande seus filhos
    betas1 = deepcopy(betas)        
    ramo1 = deepcopy(ramo)
    filhos = ramo[i].betaexp(ramo)
    ramo = ramo1
    for c in filhos:  
      ramo.append(c)
      imprime(c, "β", ramo[i])
      size_up_betas(ramo, betas, lo+1)               
      expande(ramo, betas, lo)
      if (printou_contra): return                 
      trim(ramo, lo+1)                # Vamos dar pop até a posição que estamos, (hi)
      betas = betas1      
  else:                             # Se chegou aqui, não tem mais oquê expandir.
    if(check(ramo)):
      print("Contra exemplo:")      # Vamos mostrar o ramo coerente
      show(ramo)  
      printou_contra = True

def tableaux(argumento):
  """" Inicializa um Tableau com o sequente do argumento.
       Retorna VERDADEIRO se o sequente é correto ou FALSO e
       demonstra um contraexemplo caso contrário.
  """
  ramo = deque()
  for d in argumento.premises:
    d.mark('T')
    ramo.append(d)

  argumento.conclusion.mark('F')
  ramo.append(argumento.conclusion)

  ramo1 = deepcopy(ramo)

  betas = []

  size_up_betas(ramo1, betas, 0)
  show(ramo1)
  print()
  expande(ramo1, betas, 0)
  if(not printou_contra):
    print("VERDADEIRO")

## main sendo usada para testar os argumentos
def main():
  tableaux(a)


if __name__ == "__main__":
  main()