import flet as ft
from markdown_it.common.html_re import double_quoted


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    #🙈
    def handle_analizza(self, e):

        self._view.txt_result.controls.clear()
        distance = self._view.txt_miglia.value
        #converto in intero
        try:
            distance = int(distance)
        except ValueError:
            self._view.create_alert("Inserire un valore corretto")
            return

        #se è tutto okay chiamo il metodo di model
        self._model.buildGraph(distance)

        self._view.txt_result.controls.append(ft.Text("grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"grafo contiene: {self._model.getNumNodiCoinvolti()} nodi"))
        self._view.txt_result.controls.append(ft.Text(f"grafo contiene: {self._model.getNumArchi()} archi"))

        self._view.txt_result.controls.append(ft.Text(f"Archi:"))
        for i in self._model.getArchi():
            self._view.txt_result.controls.append(ft.Text(f"-{i}"))

        self._view.update_page()
