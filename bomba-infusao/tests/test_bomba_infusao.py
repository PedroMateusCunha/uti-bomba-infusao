import pytest
import sys
import os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root)
from bomba_infusao import *

@pytest.fixture
def bomba():
    return BombaDeInfusao()

def test_inicializacao(bomba):
    assert bomba.qtd_med1 == 0
    assert bomba.qtd_med2 == 0
    assert bomba.qtd_soro == 0
    assert bomba.taxa_med1 == 0
    assert bomba.taxa_med2 == 0
    assert bomba.taxa_soro == 0
    assert not bomba.ligado

def test_set_quantidade(bomba):
    bomba.set_quantidade('med1', 10)
    assert bomba.qtd_med1 == 10

    bomba.set_quantidade('med2', 20)
    assert bomba.qtd_med2 == 20

    bomba.set_quantidade('soro', 30)
    assert bomba.qtd_soro == 30

def test_set_taxa(bomba):
    bomba.set_taxa('med1', 5)
    assert bomba.taxa_med1 == 5

    bomba.set_taxa('med2', 8)
    assert bomba.taxa_med2 == 8

    bomba.set_taxa('soro', 3)
    assert bomba.taxa_soro == 3

def test_get_quantidade(bomba):
    bomba.qtd_med1 = 15
    assert bomba.get_quantidade('med1') == 15

    bomba.qtd_med2 = 25
    assert bomba.get_quantidade('med2') == 25

    bomba.qtd_soro = 35
    assert bomba.get_quantidade('soro') == 35

def test_ligar_desligar(bomba):
    bomba.ligar()
    assert bomba.ligado

    bomba.desligar()
    assert not bomba.ligado

def test_get_status(bomba):
    bomba.set_quantidade('med1', 10)
    bomba.set_taxa('med1', 5)
    bomba.ligar()

    status = bomba.get_status()
    assert status == {
        "bomba_infusao": {
            "quantidades": {
                "med1": 10,
                "med2": 0,
                "soro": 0
            },
            "taxas": {
                "med1": 5,
                "med2": 0,
                "soro": 0
            },
            "ligado": True
        }
    }