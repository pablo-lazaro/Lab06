import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._ddAnnoValue = None
        self._ddProdottoValue = None
        self._ddRetailerValue = None

    def handleTopVendite(self, e):
        pass

    def handleAnalizzaVendite(self, e):
        pass

    def fillAnni(self):
        # Recupera i dati dal modello
        anni = self._model.getAllAnni()

        if anni is None:
            return

        for c in anni:
            # USARE _ddAnno (come definito nella View) e non ddCorsi
            self._view._ddAnno.options.append(ft.dropdown.Option(
                key=c,  # La key deve essere una stringa
                text=c,
                data=c,
                on_click=self._choiceDDAnno
            ))
        # Opzionale: aggiorna la pagina se chiami questa funzione dopo il caricamento
        self._view.update_page()

    def _choiceDDAnno(self, e): # arriva l'evento, leggiamo la selezione dell'utente e la salviamo in una variabile locale
        self._ddAnnoValue = e.control.data # --> oggetto di tipo corso che è stato selezionato dall'utente, è cui che si salva la variabile che usiamo nelle funzioni
        print(self._ddAnnoValue)

    def fillBrand(self):

        # Recupera i dati dal modello
        prodotti = self._model.getAllProdotti()

        if prodotti is None:
            return

        for c in prodotti:
            # USARE _ddAnno (come definito nella View) e non ddCorsi
            self._view._ddBrand.options.append(ft.dropdown.Option(
                key=c,  # La key deve essere una stringa
                text=c,
                data=c,
                on_click=self._choiceDDAnno
            ))
        # Opzionale: aggiorna la pagina se chiami questa funzione dopo il caricamento
        self._view.update_page()

    def _choiceDDProdotto(self, e): # arriva l'evento, leggiamo la selezione dell'utente e la salviamo in una variabile locale
        self._ddProdottoValue = e.control.data # --> oggetto di tipo corso che è stato selezionato dall'utente, è cui che si salva la variabile che usiamo nelle funzioni
        print(self._ddProdottoValue)

    def fillRetailer(self):

        # Recupera i dati dal modello
        retailer  = self._model.getAllRetailer()

        if retailer is None:
            return

        for c in retailer:
            # USARE _ddAnno (come definito nella View) e non ddCorsi
            self._view._ddRetailer.options.append(ft.dropdown.Option(
                key=c,  # La key deve essere una stringa
                text=c,
                data=c,
                on_click=self._choiceDDAnno
            ))
        # Opzionale: aggiorna la pagina se chiami questa funzione dopo il caricamento
        self._view.update_page()

    def _choiceDDRetailer(self, e): # arriva l'evento, leggiamo la selezione dell'utente e la salviamo in una variabile locale
        self._ddRetailerValue = e.control.data # --> oggetto di tipo corso che è stato selezionato dall'utente, è cui che si salva la variabile che usiamo nelle funzioni
        print(self._ddRetailerValue)