import numpy as np

# Problem definitions
p_KJ = 1e-5
p_HB = 0.5
p_HB_given_KJ = 0.9
# Question: p(KJ | HB) ?
# p(KJ | HB) = p(HB | KJ) p(KJ) / p(HB)

KJ = np.asarray([1-p_KJ, p_KJ]).reshape((2,1))
HB = np.zeros((2,2))
HB[1,0] = 0.1
HB[1,1] = 0.9
HB[0,:] = 1 - HB[1,:]
print(HB)

joint = KJ * HB

p = joint[1,1].sum()*p_KJ / joint[1,:].sum()

print(f'p( KJ | HB ) = {p:0.3f}')
