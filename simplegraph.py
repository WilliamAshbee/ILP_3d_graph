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



ab = LpVariable('ab', cat="Binary")
ac = LpVariable('ac', cat="Binary")
ad = LpVariable('ad', cat="Binary")
bc = LpVariable('bc', cat="Binary")
bd = LpVariable('bd', cat="Binary")
cd = LpVariable('cd', cat="Binary")
edges = [(ab,1),(ac,1),(ad,1.5),(bc,1.5),(bd,1),(cd,1)]

#Objective Function
obj = LpAffineExpression(edges)
print (obj)
problem+= obj
#for edge in edges:
#    problem += edge, 'Objective Function'
#Constraints

problem += ab + ac + ad >= 2
problem += ab + bc + bd >= 2
problem += ac + bc + cd >= 2
problem += ad + bd + cd >= 2 

print("Current Status: ", LpStatus[problem.status])

problem.solve()
print("ab", ab.varValue)
print("ac", ac.varValue)
print("ad", ad.varValue)
print("bc", bc.varValue)
print("bd", bd.varValue)
print("cd", cd.varValue)

print("Total edges: ", value(problem.objective))

print(problem.objective)
for a,b in enumerate(problem.constraints):
    print(a,b)