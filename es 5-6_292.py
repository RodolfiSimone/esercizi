class Prodotto:
    def __init__(self, nome , categoria , disponibilità):
        self.nome = nome
        self.categoria = categoria
        self.disponibilità = disponibilità
    
    def assegna_prezzo(self, prezzo):
        self.prezzo = prezzo
