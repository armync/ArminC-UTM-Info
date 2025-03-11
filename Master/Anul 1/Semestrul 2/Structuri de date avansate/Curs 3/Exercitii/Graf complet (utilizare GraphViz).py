import graphviz

g = graphviz.Graph(format="png")
g.engine = "circo"

n = int(input("Numarul de varfuri: "))

for varf in range(1, n+1):
    g.node(str(varf))

for varf in range(1, n+1):
    for vecin in range(varf+1, n+1):
        g.edge(str(varf), str(vecin))

g.view()
