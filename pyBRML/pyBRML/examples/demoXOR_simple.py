import numpy as np

# Problem definitions
p_A = 0.65
p_B = 0.77

# Set up potentials
A = np.asarray([1-p_A, p_A]).reshape((2,1,1))
B = np.asarray([1-p_B, p_B]).reshape((1,2,1))

# p( C | A,B )
C = np.zeros((2,2,2))
C[0,0,1] = 0.1
C[0,1,1] = 0.99
C[1,0,1] = 0.8
C[1,1,1] = 0.25
C[:,:,0] = 1 - C[:,:,1]

# Generate joint potential defined by p(A,B,C) = p( C | A,B ) p(A) p(B)
joint = A * B * C

# What is p( A=1 | C=0 )?
#
#  p(A=1,C=0)  
# -----------
#   p(C=0)
#
# - requires marginalization over B
num = joint[1,:,0].sum()
den = joint[:,:,0].sum()

print(f'p(A=1 | C=0) = {num/den:0.2f}')
