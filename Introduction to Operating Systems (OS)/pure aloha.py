import random as r

n = 5 # number of stations transmitting
p = 0.2 # the probability each individual node will transmit 
G = n * p #G = n * p so here G would be 0.5, the most efficient total probability of a transmission
frame_times = 100000 # the number of frame transmission times we will run the algorithm to get more results
successes = 0#how many successful transmissions we get


def pure_aloha(nodes):
    transmissions = sum(1 for _ in range(nodes) if r.random() < p)# if random less than p, then transmit
    if transmissions == 1:# returns true for a success with no collisions
        return True
    else:#false for a failure with either at least one collision or not transmissions at all
        return False

i = 0
while i < frame_times:#loop through however many frame times you want the test pool to be
    if(pure_aloha(n) and pure_aloha(n)): # we run the algorithm twice as the vulnerability period is twice the frame transmission time, if there i
        successes += 1#if there is a success, increment by 1
    i += 1

efficiency = successes / frame_times # how many successes per frame transmission times
print(efficiency)

def pure_aloha(n,p,frame_times):
    #n is number of stations transmitting
    #p is the probability each individual node will transmit 
    #frame_times is the number of frame transmission times we will run the algorithm to get more results

    G = n * p #G = n * p so here G would be 0.5, the most efficient total probability of a transmission
    successes = 0#how many successful transmissions we get

    i = 0
    while i < frame_times:
        transmissions = sum(1 for _ in range(n * 2) if r.random() < p)# if random less than p, then transmit
        if transmissions == 1:# returns true for a success with no collisions
            successes += 1
        i += 1

    efficiency = successes / frame_times # how many successes per frame transmission times
    print(efficiency)

pure_aloha(5,0.2,1000)