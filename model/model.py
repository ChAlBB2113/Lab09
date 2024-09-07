import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodi={}
        self._archi=[]
        self._grafo=nx.Graph()

    def creaGrafo(self, x):
        self._grafo.clear()
        self._nodi.clear()
        self._archi.clear()

        diz=DAO.getArrivoPartenzaMedia()
        self._nodi=DAO.getAereoporti()

        for k in diz:
            peso=0
            if (k not in self._grafo.edges()): #ordine nodi non importa in un grafo non orientato, trova cmq arco
                if ((k[1], k[0]) in diz):
                    peso= (diz[k]+diz[(k[1], k[0])])/2
                else:
                    peso= diz[k]
                if (peso>x): #prof in sua soluzione usa > non >= anche se in testo c'è scritto almeno
                    self._grafo.add_edge(self._nodi[k[0]],self._nodi[k[1]],weight=float(peso))
                    #float cosi tengo una cifra dopo virgola come in soluozione prof

                    #nodi vengono automaticamente creati se appartenenti a archi aggiunti;

        #ora ho fatto archi tra aeroporti che sono collegati da almeno un volo e con distanza media almeno x
        #ma cmq nel grafo voglio tutti gli aeroporti


        for chiave in self._nodi:
            if chiave not in self._grafo.nodes():
                self._grafo.add_node(chiave)












