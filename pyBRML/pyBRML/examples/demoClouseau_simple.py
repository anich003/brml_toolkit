"""
Simple implementation of demoClouseau.m in python using numpy to handle broadcasting

In this example, the joint probability can be modeled as a 2x2x2 tensor.

Here, each dimension corresponds to a variable (knife, maid, butler) and the size 
of the dimension correspond to the number of states each variable can take. 

For example,
     knife: {     used,     not_used } => 2 states
      maid: { murderer, not_murderer } => 2 states
    butler: { murderer, not_murderer } => 2 states

Author: Aaron Nichols
Date: May 3, 2018
"""
import numpy as np

# Projects each potential into its corresponding dimension
butler = np.array([0.4, 0.6]).reshape(1,1,2)
maid = np.array([0.8, 0.2]).reshape(1,2,1)

knife = np.zeros((2,2,2))
knife[1,0,0] = 0.0 # 0.3
knife[1,1,0] = 0.04 #.2
knife[1,0,1] = 0.64 #0.6
knife[1,1,1] = 0.0 # 0.1
knife[0,:,:] = 1 - knife[1,:,:]

joint = knife * butler * maid

# Set knife=1 and marginalize over maid. Normalize to knife=1
prob = joint[1,:,1].sum() / joint[1,:,:].sum()
print(f'prob( butler | knife ) = {prob:0.2f}')
