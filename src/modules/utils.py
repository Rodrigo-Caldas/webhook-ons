"""Funções utilitárias."""

import re
import unicodedata


def normalize(string: str, replacer: str = "_") -> str:
    """Padroniza uma string, removendo acentos e caracteres especiais."""
    # remove os acentos e substitui por caracteres acentuados por equivalentes
    string = (
        unicodedata.normalize("NFD", string).encode("ascii", "ignore").decode("utf-8")
    )
    # Remove especiais (e.g. @, #, $, %, &, etc.), bem como números.
    string = re.sub("[^A-Za-z0-9]+", replacer, string).strip(replacer)
    return string.lower()
