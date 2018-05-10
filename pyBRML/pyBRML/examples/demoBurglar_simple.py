"""

p(B,E,A,R) = p(A|B,E,R) p(B,E,R)
           = p(A|B,E,R) p(R|B,E) p(B,E)
           = p(A|B,E,R) p(R|B)   p(B|E) p(E)
           = p(A|B,E,R) p(R|B)   p(B)   p(E)

Variables, states, and dimensions
Alarm      (A) 0 [false,true]
Burgled    (B) 1 [false,true]
Earthquake (E) 2 [false,true]
Radio      (R) 3 [false,true]

"""
import numpy as np

p_B = 0.01
p_E = 0.000001

B = np.array([1-p_B, p_B]).reshape((1,2,1,1))
E = np.array([1-p_E, p_E]).reshape((1,1,2,1))
R = np.zeros((1,1,2,2))
R[:,:,1,1] = 1
R[:,:,0,0] = 1
A = np.zeros((2,2,2,1))
A[1,1,1] = 0.9999
A[1,1,0] = 0.99
A[1,0,1] = 0.99
A[1,0,0] = 0.0001

joint = A * R * B * E

# p(B=1|A=1)
#           A,B,E,R
num = joint[1,1,:,:].sum()
den = joint[1,:,:,:].sum()

print(f'    p(B=1|A=1) = {num/den:0.4f}')
print(f'p(B=1|A=1,R=1) = {joint[1,1,:,1].sum()/joint[1,:,:,1].sum():0.4f}')
