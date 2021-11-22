#https://www.realpythonproject.com/basic-linear-programming-in-python-with-pulp/

#pip install pulp
from pulp import *
#  
#      a-b
#      | |
#      c-d
#
#
#
#
problem = LpProblem('Car Factory', LpMinimize)


weights = [1,1,1.5,1.5,1,1]
edges = []
for i in range (6):
    s = 't'+str(i)
    edges.append((LpVariable(s, cat="Binary"),weights[i]))
# ab = LpVariable('ab', cat="Binary")
# ac = LpVariable('ac', cat="Binary")
# ad = LpVariable('ad', cat="Binary")
# bc = LpVariable('bc', cat="Binary")
# bd = LpVariable('bd', cat="Binary")
# cd = LpVariable('cd', cat="Binary")
# edges = [(ab,1),(ac,1),(ad,1.5),(bc,1.5),(bd,1),(cd,1)]

#Objective Function
obj = LpAffineExpression(edges)
print (obj)
problem+= obj
#for edge in edges:
#    problem += edge, 'Objective Function'
#Constraints

numedges = len(edges)

# e1c = LpAffineExpression([edges[0], edges[1], edges[2]])
# print('e1c',e1c)
# e1c = LpConstraint(e=e1c, sense=1, name='e1c', rhs=2)
# problem += e1c


nVert = 4
assert numedges == nVert*(nVert-1)//2

count = 0
expl = []
vc = 1
for edge in edges:
    
    if count%(nVert-1) == 0:
        expl = []
        expl.append(edge)
        
    elif count%(nVert-1)== (nVert-2):
        vc+=1
        expl.append(edge)
        print(len(expl))
        assert len(expl)==3
        ec = LpAffineExpression(expl)
        ec = LpConstraint(e=ec, sense=1, name='ed_con_'+str(vc), rhs=2)
        problem += ec
    else:
        expl.append(edge)
    count+=1   

print(vc)
assert vc == 4
# problem += ab + ac + ad >= 2
# problem += ab + bc + bd >= 2
# problem += ac + bc + cd >= 2
# problem += ad + bd + cd >= 2 

print("Current Status: ", LpStatus[problem.status])

problem.solve()

for edge in edges:
    print('edge',edge[1],edge[0].varValue)

print("Total edges: ", value(problem.objective))

print(problem.objective)
for a,b in enumerate(problem.constraints):
    print(a,b)