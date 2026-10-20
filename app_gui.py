"""
Interface Gráfica Desktop (Tkinter / ttk) do Sistema de Inteligência de Preços em Python.

Conecta as 6 abas operacionais (Busca Geral, Busca Unificada, Confronto CSV, Monitor,
Encartes e Configurações) diretamente ao motor assíncrono em Python (`pesquisa_preco_v4.py`).
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from typing import List
from pesquisa_preco_v4 import (
    ProdutoCatalogo,
    CotacaoConcorrente,
    ValidadorGS1,
    MotorCasamentoProdutos,
    ColetorAssincronoPrecios,
)


class AplicativoPriceIntelligence(tk.Tk):
    """Aplicativo Desktop em Python para operação pelo time comercial e de precificação."""

    ABAS = [
        "1. Busca Geral",
        "2. Busca Unificada",
        "3. Confronto CSV",
        "4. Monitor de Preços",
        "5. Encartes (OCR/IA)",
        "6. Configurações & Saúde",
    ]

    def __init__(self) -> None:
        super().__init__()
        self.title("Price Intelligence — Motor Python de Inteligência Competitiva")
        self.geometry("1280x760")
        self.coletor = ColetorAssincronoPrecios(concorr_maxima=8, timeout_segundos=10.0)
        self._construir_interface()

    def _construir_interface(self) -> None:
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        for nome_aba in self.ABAS:
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=nome_aba)


if __name__ == "__main__":
    app = AplicativoPriceIntelligence()
    app.mainloop()
