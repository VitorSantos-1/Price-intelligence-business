"""Testes unitarios das funcoes puras de validacao/normalizacao (sem dependencias externas)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pesquisa_preco_v4 import ValidadorGS1, MotorCasamentoProdutos


def test_limpar_ean_remove_nao_digitos():
    assert ValidadorGS1.limpar_ean("789 100-0315507") == "7891000315507"


def test_limpar_ean_none_vira_vazio():
    assert ValidadorGS1.limpar_ean(None) == ""


def test_ean_valido_ean13_correto():
    assert ValidadorGS1.ean_valido("4006381333931") is True


def test_ean_valido_digito_verificador_errado():
    assert ValidadorGS1.ean_valido("4006381333930") is False


def test_ean_valido_curto_ou_none():
    assert ValidadorGS1.ean_valido("123") is False
    assert ValidadorGS1.ean_valido(None) is False


def test_normalizar_texto_minusculo_e_espacos():
    assert MotorCasamentoProdutos.normalizar_texto("  Cafe   TORRADO ") == "cafe torrado"
