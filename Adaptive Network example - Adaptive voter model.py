import networkx as nx
import matplotlib.pyplot as plt
import random
import networkx as nx



N = 100    # No of nodes
edge_p = 0.05   # Probability of creation of edges
rewrite_p = 0.5  # Probability of rewriting node opinion
max_steps = 500


G = nx.erdos_renyi_graph(N,edge_p)   # makes a random graph


# Now lets assign a opinion to each node

for i in G.nodes() :
    G.nodes[i]["opinion"] = random.choice([0,1])  # Assigns a random opinion out of 1 and 0 to all nodes

def voter_adaptive_model(G,p):
    if G.number_of_edges() == 0 :   # if no edges are there the system will not evolve
        return
    
    A,B = random.choice(list(G.edges()))   # Choosing a random node to adapt

    opinion_A = G.nodes[A]['opinion']
    opinion_B = G.nodes[B]['opinion']

    if opinion_A != opinion_B :  # If opinion of node A is not equal to node B, we have 2 options. Either rewrite the node or break the edge between node A and B.

        if random.random() < rewrite_p :  # checking probability rewrite or break

            G.remove_edge(A,B) # break edge

             #find new node to connect out node

            potential_nodes = [i for i in list(G.nodes())              
                               if opinion_A == G.nodes[i]['opinion']  # new node has to have same opinion
                               if not G.has_edge(A,i)    #new node cant have an edge with our node
                               if A != i]    # nad make sure new node is same as old node
            
            if len(potential_nodes) != 0 :  # check if there is a new node
                new_partner = random.choice(potential_nodes)
                G.add_edge(A,new_partner) # Add a edge between new node and old node

        else : 


            G.nodes[A]["opinion"] = opinion_B

def counting_active_links(G):   # Active Links : edge with both nodes having different opinon

    return  sum(1 for A,B in G.edges if G.nodes[A]['opinion']!= G.nodes[B]['opinion'] )



def opinion_value(G) :    # fraction of nodes with opinion 1 

    return sum(1 for i in G.nodes if G.nodes[i]['opinion']==1)/N


active_links_val = []
opinion_frac_val = [] 


for i in range(max_steps) :

    voter_adaptive_model(G,rewrite_p)

    v = counting_active_links(G)
    active_links_val.append(v)

    o = opinion_value(G)
    opinion_frac_val.append(o)

    if v == 0 :  # if there are no active links, ie there are no nodes connected with different opinion, our adaptive model stops evolving
        break

# Plotting results
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(active_links_val, color='red')
plt.xlabel("Time step")
plt.ylabel("Number of active links")
plt.title("Number of Disagreement Edges Over Time")

plt.subplot(1, 2, 2)
plt.plot(opinion_frac_val, color='blue')
plt.xlabel("Time step")
plt.ylabel("Fraction of opinion = 1")
plt.title("Fraction of Opinion 1 Over Time")

plt.tight_layout()
plt.show()







