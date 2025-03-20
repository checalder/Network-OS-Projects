import random
import matplotlib.pyplot as plt
import numpy as np

def simulate_slotted_aloha(n_nodes, p, n_slots):
    # n_nodes: number of nodes in the network
    # p: probability of transmitting in a slot
    # n_slots: number of slots to simulate

    successes = 0 # Number of successful transmissions

    # Loop over each slot in the simulation
    for _ in range(n_slots):
        # Each node transmits with probability p in a slot        
        # only if a single node transmits in a slot, it is a success
        # so say we have for each node 0.1, 0.5, 0.3, 0.2 the total 
        
        transmissions = sum(1 for _ in range(n_nodes) if random.random() < p)
        # adds 1 to the sum if random.random() < p,
    if transmissions == 1:# transmissions will be 2 as [0] and [3] are less than p (0.3) and so 
        #we would not have a success in our example
        successes += 1
    # then the same loop will be repeated for the next slot and so forth until the n_slots are reached
    efficiency = successes / n_slots
    #then we see how many successes we had and can calculate efficienct
    return efficiency

#here we are just plotting the efficiency of the slotted aloha for different values of p using matplotlib

n_nodes = 50
ps = np.linspace(0, 1, 50)
efficiencies = [simulate_slotted_aloha(n_nodes, p, 10000) for p in ps]
plt.plot(ps, efficiencies, marker='o')
plt.xlabel('Transmission Probability')
plt.ylabel('Efficiency')
plt.title('Slotted ALOHA Efficiency Simulation')
plt.show()