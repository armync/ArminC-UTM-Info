import graphviz


def DFS(vf_crt, lista_comp_conexa):
    global vizitat

    vizitat[vf_crt] = True
    lista_comp_conexa.append(vf_crt)
    for vecin in lista_adiacenta[vf_crt]:
        if vizitat[vecin] == False:
            DFS(vecin, lista_comp_conexa)


fin = open("graf.txt")
nr_varfuri = int(fin.readline())

g = graphviz.Graph(format="png")
g.engine = "circo"

for varf in range(1, nr_varfuri+1):
    g.node(str(varf))

lista_adiacenta = {vf: [] for vf in range(1, nr_varfuri+1)}

for muchie in fin:
    aux = muchie.split()
    x = int(aux[0])
    y = int(aux[1])
    lista_adiacenta[x].append(y)
    lista_adiacenta[y].append(x)
    g.edge(str(x), str(y))

fin.close()

vizitat = [False] * (nr_varfuri+1)
componente_conexe = []
while True:
    try:
        vf_start = vizitat.index(False, 1)
        componente_conexe.append([])
        DFS(vf_start, componente_conexe[-1])
    except ValueError:
        break

print("Componentele conexe:")
for cc_crt in componente_conexe:
    print(*cc_crt)

for cc_crt in range(len(componente_conexe)):
    for vf_crt in componente_conexe[cc_crt]:
        g.node(str(vf_crt), color="/set19/"+str(cc_crt%9+1), style="filled")

g.view()