graph = Graph.from_json("./State_Data/Tract20.json")
df = gpd.read_file("./State_Data/Tract20.shp")
centroids = df.centroid
c_x = centroids.x
c_y = centroids.y
totpop = 0
for n in graph.nodes():
    graph.node[n]["TOTPOP"] = int(graph.node[n]["TOTPOP"])

    totpop += graph.node[n]["TOTPOP"]

cddict = recursive_tree_part(graph, [-1, 1], totpop / 2, "TOTPOP", .05, 1)

for n in graph.nodes():
    graph.node[n]["part_sum"] = cddict[n]
    graph.node[n]["last_flipped"] = 0
    graph.node[n]["num_flips"] = 0

for edge in graph.edges():
    graph[edge[0]][edge[1]]['cut_times'] = 0

pos = {node: (c_x[node], c_y[node]) for node in graph.nodes}

updaters = {'population': Tally('TOTPOP', alias="population"),
            # "boundary":bnodes_p,
            # "slope": boundary_slope,
            'cut_edges': cut_edges,
            'step_num': step_num,
            'b_nodes': b_nodes_bi,
            'base': new_base,
            'geom': geom_wait,
            # "Pink-Purple": Election("Pink-Purple", {"Pink":"pink","Purple":"purple"})
            }

#########BUILD PARTITION

grid_partition = Partition(graph, assignment=cddict, updaters=updaters)

# ADD CONSTRAINTS
popbound = within_percent_of_ideal_population(grid_partition, pop1)

ns = 25
plt.figure(figsize=(10,5))
nx.draw(graph, pos=pos, node_color=[dict(grid_partition.assignment)[x] for x in graph.nodes()], node_size=ns,
        cmap='tab20', node_shape='o')
plt.savefig("./plots/States/Dual_graph_Kansas_start.png")
plt.close()

plt.figure(figsize=(10,5))
df["starting"] = df.index.map(dict(grid_partition.assignment))
df.plot(column="starting", cmap='tab20')
plt.axis('off')
plt.savefig("./plots/States/Kansas_start.png")
plt.close()


