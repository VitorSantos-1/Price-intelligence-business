"""
Script Python de Empacotamento Automático em Executável (.exe) via PyInstaller.
"""

import subprocess
import sys
from pathlib import Path


def empacotar_executavel() -> None:
    comando = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--onefile",
        "--windowed",
        "--name",
        "PesquisaPreco_v4",
        "app_gui.py",
    ]
    print("Executando PyInstaller via Python:", " ".join(comando))
    subprocess.run(comando, check=True)


if __name__ == "__main__":
    empacotar_executavel()
