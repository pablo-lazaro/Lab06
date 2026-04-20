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
        # 1. Recupero Anno
        valore_anno = self._view._ddAnno.value # Potrei anche mettere la variabile che ho salvato usando una funzione choice

        anno = int(valore_anno) if (valore_anno and valore_anno != "Nessun Filtro") else None

        # 2. Recupero Brand
        valore_brand = self._view._ddBrand.value # Potrei anche mettere la variabile che ho salvato usando una funzione choice
        brand = valore_brand if (valore_brand and valore_brand != "Nessun Filtro") else None

        # 3. Recupero Retailer Code
        # Se hai salvato la key come r.code nel dropdown:
        valore_retailer = self._view._ddRetailer.value
        retailer_code = int(valore_retailer) if (valore_retailer and valore_retailer != "Nessun Filtro") else None

        # Chiamata al model
        results = self._model.getTopVendite(anno, brand, retailer_code)

        # Pulizia e stampa
        self._view.txt_result.controls.clear()
        if not results:
            self._view.txt_result.controls.append(ft.Text("Nessun risultato trovato."))
        for v in results:
            self._view.txt_result.controls.append(ft.Text(v.__str__()))
        self._view.update_page()



    def handleAnalizzaVendite(self, e):
        self._view.txt_result.controls.clear()

        # Leggiamo i valori dai dropdown
        anno = self._view._ddAnno.value
        brand = self._view._ddBrand.value
        retailer_code = self._view._ddRetailer.value

        # Gestione filtri opzionali per COALESCE
        # Se il valore è "Nessun Filtro" o None, lo trasformiamo in None per il DB
        anno_val = int(anno) if (anno and anno != "Nessun Filtro") else None
        brand_val = brand if (brand and brand != "Nessun Filtro") else None
        retailer_val = int(retailer_code) if (retailer_code and retailer_code != "Nessun Filtro") else None

        stats = self._model.getStatistiche(anno_val, brand_val, retailer_val)

        if stats and stats['NumeroVendite'] > 0:
            self._view.txt_result.controls.append(ft.Text("Statistiche vendite:", weight="bold"))
            self._view.txt_result.controls.append(ft.Text(f"Giro d'affari: {stats['GiroAffari']:.2f}"))
            self._view.txt_result.controls.append(ft.Text(f"Numero vendite: {stats['NumeroVendite']}"))
            self._view.txt_result.controls.append(ft.Text(f"Numero retailers coinvolti: {stats['NumeroRetailers']}"))
            self._view.txt_result.controls.append(ft.Text(f"Numero prodotti coinvolti: {stats['NumeroProdotti']}"))
        else:
            self._view.txt_result.controls.append(ft.Text("Nessuna vendita trovata con i filtri selezionati."))

        self._view.update_page()

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
        prodotti = self._model.getAllBrand()

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
                key=str(c.code),  # La key deve essere una stringa
                text=c.name,
                data=c,
                on_click=self._choiceDDAnno
            ))
        # Opzionale: aggiorna la pagina se chiami questa funzione dopo il caricamento
        self._view.update_page()

    def _choiceDDRetailer(self, e): # arriva l'evento, leggiamo la selezione dell'utente e la salviamo in una variabile locale
        self._ddRetailerValue = e.control.data # --> oggetto di tipo corso che è stato selezionato dall'utente, è cui che si salva la variabile che usiamo nelle funzioni
        print(self._ddRetailerValue)