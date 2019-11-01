"""Arquivo com os testes de operacoes"""

from com.faculdadeimpacta.calculadora.operacoes import soma

def test_soma():
    """Teste da operacao soma"""
    assert soma(1, 2) == 3, 'Deveria ser 3'
