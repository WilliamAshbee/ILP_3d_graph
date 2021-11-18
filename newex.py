#https://www.realpythonproject.com/basic-linear-programming-in-python-with-pulp/

#pip install pulp
from pulp import *

problem = LpProblem('Car Factory', LpMaximize)

A = LpVariable('Car A', lowBound=0 , cat=LpInteger)
B = LpVariable('Car B', lowBound=0 , cat=LpInteger)

#Objective Function
problem += 20000*A + 45000*B, 'Objective Function'
#Constraints
problem += 4*A + 5*B <= 30, 'Designer Constraint'
problem += 3*A + 6*B <= 30, 'Engineer Constraint'
problem += 2*A + 7*B <= 30, 'Machine Constraint'

print("Current Status: ", LpStatus[problem.status])

problem.solve()
print("Number of Car A Made: ", A.varValue)
print("Number of Car B Made: ", B.varValue)
print("Total Profit: ", value(problem.objective))

