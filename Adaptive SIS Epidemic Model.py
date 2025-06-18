import networkx as nx
import matplotlib.pyplot as plt
import random


N = 100
p = 0.1
beta = 0.5 # Infection probability
mue = 0.2 # recovery probability
omega = 0.3 #re-wiring probability
t_heal = 20
max_step = 1000

G = nx.erdos_renyi_graph(N,p)

for i in G.nodes() :
    G.nodes[i]['state'] = random.choice(["S","I"])
    G.nodes[i]['t'] = 0


def time_infection(G):
    for i in G.nodes() :
        if G.nodes[i]['state'] == "I":
            G.nodes[i]['t'] += 1

def infection(G) :
    if len(G.edges()) == 0 :
        return
    
    A,B = random.choice(list(G.edges()))

    # Infection

    if G.nodes[A]['state'] == "S" and G.nodes[B]['state']== "I":

        r = random.random()

        if r < beta :

            G.nodes[A]['state'] = "I"

        elif r < beta+omega :

            G.remove_edge(A,B)

            potential_nodes = [i for i in list(G.nodes())
                               if G.nodes[i]['state'] == "S"
                               if not G.has_edge(A,i)
                               if A != i] 
            
            if len(potential_nodes) != 0 :
                new_partner = random.choice(potential_nodes)
                G.add_edge(A,new_partner)
            
        else :
            pass
    
    else:
        pass

def recovery(G):

    for i in G.nodes() :
        if G.nodes[i]['state'] == "I" and G.nodes[i]['t'] >= t_heal and random.random()< mue :
            G.nodes[i]['state'] = "S"
            G.nodes[i]['t'] = 0
        else :
            pass



def count_active_links(G):
    return sum(1 for A,B in G.edges() if G.nodes[A]['state']!=G.nodes[B]['state'])

def infection_fraction(G):
    return sum(1 for i in G.nodes() if G.nodes[i]['state'] == "I")/N

active_links_val = []
infection_fraction_val = []

for i in range(max_step):

    time_infection(G)
    recovery(G)
    infection(G)

    a = count_active_links(G)
    active_links_val.append(a)

    inf = infection_fraction(G)
    infection_fraction_val.append(inf)

# Plotting results
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(active_links_val, color='red')
plt.xlabel("Time step")
plt.ylabel("Number of active links")
plt.title("Number of Edges with posibility of transmitting infection Over Time")

plt.subplot(1, 2, 2)
plt.plot(infection_fraction_val, color='blue')
plt.xlabel("Time step")
plt.ylabel("Fraction of infected people")
plt.title("Fraction of infected nodes Over Time")

plt.tight_layout()
plt.show()



    
