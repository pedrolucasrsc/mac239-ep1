from collections import deque
from code_base_EP1 import *


x = "(((a | b) >> q)"
operadores = [" >> ", " & ", " | ", "~"]
pa = ["(", ")"]
value = deque()
operators = deque()
for i in range(len(x)):
    if x[i] == ">": 
        x[i] = ">>"
        i += 2
    if((x[i] not in operadores) and (x[i] not in pa)):
        value.append(x[i])
    elif (x[i] in operadores):
        operators.append(x[i])
    elif (x[i] == ")"):
        op = operators.pop()
        a = value.pop()
        b = value.pop()
    else:
        continue

for j in range(0, 5):
    if j == 0:
        j += 2
    print()

