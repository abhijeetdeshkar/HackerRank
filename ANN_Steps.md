 1. Randomly initialise the weights to small numbers close to 0 (but not 0)
 2. Input the first observation of your dataset in the input layer, each feature in one input node.
 3. Forward Propogation: from left to right the neurons are activated in a way that the impact of each neuron's activation is limited by the weights. Propgate the activations until getting the predcited result y.
 4. Compare the predicted result to the actual result. Measure the generated error.
 5. Back Propogation: from right to left , the error is back propogated. Update the weights according to how much they are responsible for the error. The learning rate decides how much we update the weights.
 6. Repeat steps 1 to 5 and update the weights after each observation (Reinforcement learning) or Repeat Steps 1 to 5 but update the weights only after a batch of observations. (Batch Learning)
 7. When the whole training set passed through the ANN, that makes an epoch. Redo more epochs.

num= $pi [(x+y)^2 - (y/2)^2]$ = $pi[x^2 + y^2 + 2xy - y^2/4]$
deno = $pi(y/2)^2$ = $pi[y^2/4]$
f = $4x^2/y^2 + 4 + 8x/y - 1$
 = $4 *(1/9) + 4 + 8/3 -1$ = $28/9 + 3$ 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNjc0MTgyNDcsLTk1MDQ0MTY5M119
-->