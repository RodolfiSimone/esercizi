class Atleta:
    def __init__(self, nome , eta , sport, visita_medica):
        self.nome = nome
        self.eta = eta
        self.sport = sport
        self.visita_medica = visita_medica

    def squadra(self, squadra):
        self.squadra = squadra

    def effettua_visita(self):
        self.visita_medica = True

    def dati(self):
        print("Il giocatore", self.nome,"ha", self.eta,"anni, gioca a", self.sport,"nella squadra de", self.squadra)