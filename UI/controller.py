from operator import itemgetter

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self,e):

        input=self._view._txtIn.value

        #controllo valore sia stato inserito
        if input=="" or input==None or input=="Distanza Minima":
            self._view.alert("Inserire una distanza media minima")
            self._view.update_page() #ogni volta che codice arriva a termine al momento e deve dare in output qualcosa
            return #e ritorno cosi che il resto della funzione non vada avanti con parametro non opportuno

        #controllo valore sia numerico
        try:
            x=int(input)
            #visibile anche fuori da ciclo try/except
        except ValueError:
            #prima di scrivere qualcosa
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text(f"inserire numero intero"))
            self._view.update_page()
            return

        self._model.creaGrafo(x)

        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Numero di nodi: {len(self._model._grafo.nodes())}"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di archi: {len(self._model._grafo.edges())}"))
        #for arco in self._model._grafo.edges():
            #print(arco)
            #self._view._txt_result.controls.append(ft.Text(f"{self._model._nodi[arco[0]]} -> {self._model._nodi[arco[1]]} -- AvgDist: {self._model._grafo[arco[0]][arco[1]]['weight']}"))

        #grafo è diz di diz; chiave primaria è nodo di partenza con cui si accede a chiave secondaria che è nodo di arrivo con cui si accede
        #a valore "weight" cioe il peso dell arco
        #grafo[nodo1]= nodo 1
        #grafo[nodo1][nodo2]=valore nodo 2
        #grafo[nodo1][nodo2]['weight']= peso
        #PS. gli apici servono solo per chiavi che sono stringhe, non per numeri o variabili!

        #ordino output secondo distanza media...prof non ha ordinato ma preso archi aggregandoli subito con una query in sql quindi venuti in ordine
        #diverso dal mio....non serviva ordinare , ad ogni modo bene sapere come ordinare comodamente un grafo....
        #lo trasformo in lista di tuple e uso itemgetter;
        lista=[]
        for arco in self._model._grafo.edges():
            lista.append((arco[0], arco[1], self._model._grafo[arco[0]][arco[1]]['weight']))
        lista.sort(key=itemgetter(2), reverse=True)

        for tupla in lista:
            print(tupla)
            self._view._txt_result.controls.append(ft.Text(f"{tupla[0]} -> {tupla[1]} -- AvgDist: {tupla[2]}"))

        self._view.update_page()













