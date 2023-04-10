from fastapi import FastAPI, Request
from bomba_infusao import BombaDeInfusao

app = FastAPI()
bomba = BombaDeInfusao()

@app.get("/")
def read_root():
    return {"message": "Bomba de infusão"}

@app.get("/status")
def check_status():
    return bomba.get_status()

@app.get("/medicamento/{medicamento}")
def get_medicamentos(medicamento: str):
    return bomba.get_quantidade(medicamento)

@app.put("/medicamento/{medicamento}/{quantidade}")
def set_medicamentos(medicamentos: str, quantidade: float):
    bomba.set_quantidade(medicamentos, quantidade)
    return {"message": "Medicamentos atualizados com sucesso"}

@app.get("/taxa/{medicamento}")
def get_medicamentos(medicamento: str):
    return bomba.get_quantidade(medicamento)

@app.put("/taxa/{medicamento}/{taxa}")
def set_medicamentos(medicamentos: str, quantidade: float):
    bomba.set_quantidade(medicamentos, quantidade)
    return {"message": "Medicamentos atualizados com sucesso"}

@app.put("/ligar")
def ligar():
    bomba.ligar()
    return {"message": "Bomba de infusão ligada"}

@app.put("/desligar")
def desligar():
    bomba.desligar()
    return {"message": "Bomba de infusão desligada"}
