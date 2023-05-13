"""
Modulo para inicialização e disponilibilização do serviço
relacionado à bomba de infusão de medicamentos.
"""
from fastapi import FastAPI, Request
from bomba_infusao import BombaDeInfusao

app = FastAPI()
bomba = BombaDeInfusao()

@app.get("/")
def read_root():
    """Metodo para roteamento inicial do componente"""
    return {"message": "Bomba de infusão"}

@app.get("/status")
def check_status():
    """Metodo para roteamento de checagem de status da bomba de infusão"""
    return bomba.get_status()

@app.get("/medicamento/{medicamento}")
def get_medicamentos(medicamento: str):
    """Metodo para roteamento para recuperar os medicamentos administrados"""
    return bomba.get_quantidade(medicamento)

@app.put("/medicamento/{medicamento}/{quantidade}")
def set_medicamentos(medicamentos: str, quantidade: float):
    """Metodo para roteamento para reaizar mudanças nos medicamentos administrados"""
    bomba.set_quantidade(medicamentos, quantidade)
    return {"message": "Medicamentos atualizados com sucesso"}

@app.get("/taxa/{medicamento}")
def get_medicamentos(medicamento: str):
    """Metodo para roteamento para recuperar a quantidade de um medicamento"""
    return bomba.get_quantidade(medicamento)

@app.put("/taxa/{medicamento}/{taxa}")
def set_medicamentos(medicamentos: str, quantidade: float):
    """Metodo para roteamento para setar a quandidade de um medicamento"""
    bomba.set_quantidade(medicamentos, quantidade)
    return {"message": "Medicamentos atualizados com sucesso"}

@app.put("/ligar")
def ligar():
    """Metodo para roteamento para ativar a bomba de infusao"""
    bomba.ligar()
    return {"message": "Bomba de infusão ligada"}

@app.put("/desligar")
def desligar():
    """Metodo para roteamento para desativar a bomba de infusao"""
    bomba.desligar()
    return {"message": "Bomba de infusão desligada"}
