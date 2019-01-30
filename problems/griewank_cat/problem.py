from collections import OrderedDict
import numpy as np
import os 

np.random.seed(0)

HERE = os.path.dirname(os.path.abspath(__file__))

from ytopt.problem import Problem

cmd_frmt = "python " +HERE+"/executable.py"
nparam = 10
for i in range(1, nparam+1):
    cmd_frmt += f" --p{i} {'{}'}"
problem = Problem(cmd_frmt)

a, b = -600, 600
for i in range(nparam):
    problem.spec_dim(p_id=i, p_space= list(np.random.permutation([str(i) for i in range(a,b,50)])), default=str(a))
problem.checkcfg()

if __name__ == '__main__':
    print(problem)
