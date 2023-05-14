"""Modulo para gerenciamento da bomba de infusao do leito hospitalar."""
class BombaDeInfusao:
    """
    Classe para gerenciamento da administração e quantidades de medicação
    recebidas pelo paciente no leito hospitalar
    """
    def __init__(self):
        """
        Metodo para inicializar das quantidades de medicação e estado
        da bom da infusão
        """
        self.qtd_med1 = 0
        self.qtd_med2 = 0
        self.qtd_soro = 0
        self.taxa_med1 = 0
        self.taxa_med2 = 0
        self.taxa_soro = 0
        self.ligado = False

    def set_quantidade(self, medicamento, quantidade):
        """
        Metodo utilizado para atualizar a quantidade dos medicamentos
        administrados ao paciante.
        """
        if medicamento == 'med1':
            self.qtd_med1 = quantidade
        elif medicamento == 'med2':
            self.qtd_med2 = quantidade
        elif medicamento == 'soro':
            self.qtd_soro = quantidade

    def set_taxa(self, medicamento, taxa):
        """
        Metodo utilizado para atualizar as taxas dos medicamentos
        administrados ao paciante.
        """
        if medicamento == 'med1':
            self.taxa_med1 = taxa
        elif medicamento == 'med2':
            self.taxa_med2 = taxa
        elif medicamento == 'soro':
            self.taxa_soro = taxa

    def get_quantidade(self, item):
        """
        Metodo utilizado para recuperar a quantidade de determinado 
        medicamento.
        """
        return getattr(self, f"qtd_{item}")

    def ligar(self):
        """
        Metodo utilizado para ativar a bomba de infusão.
        """
        self.ligado = True

    def desligar(self):
        """
        Metodo utilizado para desativar a bomba de infusão.
        """
        self.ligado = False

    def get_status(self):
        """
        Metodo utilizado para recuperar o estado da bomba de infusão
        e das quantidades de medicamentos administrados ao paciente.
        """
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
