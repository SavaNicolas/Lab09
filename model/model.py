from database.DAO import DAO
import networkx as nx

from model.flights import Flights


class Model:
    #inizializzo per poi andare a costruire il grafo:
    #1-grafo vuoto
    #quelli che saranno i nodi
    #idMap per il volo
    def __init__(self):
        #mi creo il grafo non orientato in questo caso
        self._grafo= nx.Graph()
        #i nodi sono tutti gli aereoporti--> me li ricavo
        self._aereoporti= DAO.get_aereoporti()
        #mappa aereoporti per ricavare dall'id tutto quello che mi serve
        self.idMapAereoporti = {}
        for a in self._aereoporti:
            self.idMapAereoporti[a.ID] = a

    def buildGraph(self,distance):
        #aggiungo i nodi che sono gli aereoporti
        self._grafo.add_nodes_from(self._aereoporti)
        #aggiungo gli archi che dovrebbero essere i voli
        self.addEdges(distance)

    def addEdges(self,distance):
        """ aggiungo gli archi direttamente da flights in base a nodo partenza e nodo arrivo,
        in flights son sicuro che ho già almeno un 1 volo che collega glia aereoporti
        """
        all_flights= DAO.get_flights()
        for flight in all_flights:
            u= self.idMapAereoporti[flight.ORIGIN_AIRPORT_ID]
            v= self.idMapAereoporti[flight.DESTINATION_AIRPORT_ID]
            #calcolo peso arco che deve essere una media della somma delle distanze tra A-->B e B-->A
            peso= self.calcola_peso(flight.ORIGIN_AIRPORT_ID,flight.DESTINATION_AIRPORT_ID)
            if peso>=distance:
                self._grafo.add_edge(u,v, weight=peso)



    def getNumNodi(self):
        return len(self._grafo.nodes())

    def getNumArchi(self):
        return len(self._grafo.edges())

    def getArchi(self):
        return self._grafo.edges()

    def calcola_peso(self,a,b):
        voli= DAO.get_voli_ab(a,b)
        numeratore=0
        denominatore=len(voli)
        for i in voli:
            numeratore+= i.DISTANCE

        peso=numeratore/denominatore
        return peso




