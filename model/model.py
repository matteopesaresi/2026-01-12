import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._anni = DAO.getAllYears()
        self._all_vertici = {vertice.constructorId: vertice for vertice in DAO.getAllNodes()}


    def buildGraph(self,anno1,anno2):
        if anno1 > anno2:
            anno1 = anno2
        self._vertici = DAO.getNodes(anno1,anno2)
        for nodo in self._vertici:
            if nodo in self._vertici:
                id = int(nodo[0])
                vertice = self._all_vertici.get(id)
                self._graph.add_node(vertice)


