import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnni(self):
        for anno in self._model._anni:
            self._view._ddAnno1.options.append(ft.dropdown.Option(key=str(anno), text=str(anno)))
            self._view._ddAnno2.options.append(ft.dropdown.Option(key=str(anno), text=str(anno)))
        self._view.update_page()
    def handleCreaGrafo(self,e):
        pass

    def handleDettagli(self, e):
        pass

    def handleCerca(self, e):
        pass

