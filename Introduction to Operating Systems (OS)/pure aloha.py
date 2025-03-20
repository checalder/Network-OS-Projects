import random as r  # Import the random module for generating transmission probabilities

# Define parameters for the Pure ALOHA simulation
n = 5  # Number of stations transmitting
p = 0.2  # Probability that each station transmits in a time slot
G = n * p  # Traffic intensity G (expected number of transmission attempts per frame time)
frame_times = 100000  # Number of frame transmission times to simulate
successes = 0  # Counter for successful transmissions

def pure_aloha(nodes):
    """
    Simulates the transmission process in Pure ALOHA.
    
    Parameters:
        nodes (int): Number of transmitting stations.
    
    Returns:
        bool: True if exactly one station transmits (successful transmission), False otherwise.
    """
    transmissions = sum(1 for _ in range(nodes) if r.random() < p)  # Count nodes that attempt transmission
    return transmissions == 1  # Success occurs only if exactly one node transmits

# Simulating multiple frame times
i = 0
while i < frame_times:
    # Check for successful transmission in two consecutive frame times (vulnerability period is 2 frames)
    if pure_aloha(n) and pure_aloha(n):
        successes += 1  # Increment success counter
    i += 1

# Compute efficiency of Pure ALOHA (successful transmissions per frame time)
efficiency = successes / frame_times
print(efficiency)

def pure_aloha_simulation(n, p, frame_times):
    """
    Runs a Pure ALOHA simulation with given parameters.
    
    Parameters:
        n (int): Number of transmitting stations.
        p (float): Probability of transmission per station per frame time.
        frame_times (int): Number of frame times to simulate.
    
    Returns:
        None: Prints efficiency of the protocol.
    """
    G = n * p  # Traffic intensity
    successes = 0  # Counter for successful transmissions

    for _ in range(frame_times):
        transmissions = sum(1 for _ in range(n * 2) if r.random() < p)  # Simulating transmission attempts
        if transmissions == 1:
            successes += 1  # Successful transmission recorded

    efficiency = successes / frame_times  # Compute efficiency
    print(efficiency)

# Running the Pure ALOHA simulation with 5 nodes, transmission probability 0.2, and 1000 frame times
pure_aloha_simulation(5, 0.2, 1000)
