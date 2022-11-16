from sys import maxsize
from itertools import permutations
V=4
def TSP(G,s):
	vertex=[]
	for i in range(V):
		if i!=s:
			vertex.append(i)
	MP=maxsize
	NP=permutations(vertex)
	for i in NP:
		CPW=0
		k=s
		for j in i:
			CPW+=G[k][j]
			k=j
		CPW+=G[k][s]
		MP=min(MP,CPW)
	return MP
if __name__=="__main__":
	G=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
	s=0
	print(TSP(G,s))