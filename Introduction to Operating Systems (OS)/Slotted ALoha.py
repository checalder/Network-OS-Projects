import random  # Importing random module for probabilistic transmission
import matplotlib.pyplot as plt  # Importing matplotlib for plotting results
import numpy as np  # Importing NumPy for numerical operations

def simulate_slotted_aloha(n_nodes, p, n_slots):
    """
    Simulates Slotted ALOHA protocol for network communication.
    
    Parameters:
        n_nodes (int): Number of nodes in the network.
        p (float): Probability of each node transmitting in a slot.
        n_slots (int): Number of time slots to simulate.
    
    Returns:
        float: Efficiency of the Slotted ALOHA protocol.
    """
    successes = 0  # Counter for successful transmissions

    # Iterate over each time slot
    for _ in range(n_slots):
        # Count the number of nodes that attempt transmission
        transmissions = sum(1 for _ in range(n_nodes) if random.random() < p)
        
        # A successful transmission occurs if exactly one node transmits
        if transmissions == 1:
            successes += 1
    
    # Compute efficiency as the ratio of successful transmissions to total slots
    efficiency = successes / n_slots
    return efficiency

# Define the number of nodes in the network
n_nodes = 50

# Generate an array of transmission probabilities from 0 to 1
ps = np.linspace(0, 1, 50)

# Compute efficiency for different transmission probabilities
# The efficiency curve will show how transmission probability affects Slotted ALOHA performance
efficiencies = [simulate_slotted_aloha(n_nodes, p, 10000) for p in ps]

# Plot efficiency against transmission probability
plt.plot(ps, efficiencies, marker='o')
plt.xlabel('Transmission Probability')
plt.ylabel('Efficiency')
plt.title('Slotted ALOHA Efficiency Simulation')
plt.show()
