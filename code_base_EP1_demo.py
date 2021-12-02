#import code_base as CB

from code_base_EP1 import *
from argumentos import *

# fórmulas
# todos os átomos que serão utilizados nas fórmulas precisam ser declarados
P,Q,R,S = vars('P', 'Q', 'R', 'S')


print("\n")
print("a")
print("Premissas")
print(a.premises)
print("Conclusão")
print(a.conclusion)
print("Tabela Verdade")
a.print_truth_table()
print("É válido? - método Tabela Verdade") #validade calculada via tabela verdade
print(a.is_valid_truth_table())
#

#