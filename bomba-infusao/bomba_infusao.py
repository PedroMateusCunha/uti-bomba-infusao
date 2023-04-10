class BombaDeInfusao:
    def __init__(self):
        self.qtd_med1 = 0
        self.qtd_med2 = 0
        self.qtd_soro = 0
        self.taxa_med1 = 0
        self.taxa_med2 = 0
        self.taxa_soro = 0
        self.ligado = False

    def set_quantidade(self, medicamento, quantidade):
        if medicamento == 'med1':
            self.qtd_med1 = quantidade
        elif medicamento == 'med2':
            self.qtd_med2 = quantidade
        elif medicamento == 'soro':
            self.qtd_soro = quantidade

    def set_taxa(self, medicamento, taxa):
        if medicamento == 'med1':
            self.taxa_med1 = taxa
        elif medicamento == 'med2':
            self.taxa_med2 = taxa
        elif medicamento == 'soro':
            self.taxa_soro = taxa

    def get_quantidade(self, item):
        return getattr(self, f"qtd_{item}")

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def get_status(self):
        return { "bomba_infusao": {
                "quantidades": {
                    "med1": self.qtd_med1,
                    "med2": self.qtd_med2,
                    "soro": self.qtd_soro
                },
                "taxas": {
                    "med1": self.taxa_med1,
                    "med2": self.taxa_med2,
                    "soro": self.taxa_soro
                },
                "ligado": self.ligado
            }
        }