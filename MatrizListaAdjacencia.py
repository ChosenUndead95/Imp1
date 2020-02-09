import networkx as nx

G = nx.Graph()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(4,6)
G.add_edge(5,4)
G.add_edge(2,3)
G.add_edge(2,6)

matriz = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

def matrizAdj(G):
  print("Lista de Adjacencia: ")
  for i in G:
    print(i," -> ", G[i])
  print("Matriz de Adjacencia: ")
  for linha in G:
    for coluna in G:
      if linha in G[coluna]:
        matriz[linha - 1][coluna - 1] = 1
  for l in G:
    for c in G:
      print(f'[{matriz[l - 1][c - 1]}]', end='')
    print()
matrizAdj(G)
	



