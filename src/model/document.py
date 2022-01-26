from dataclasses import dataclass

@dataclass
class Filme:
    arquivo: str

@dataclass
class Documento:
    filme: Filme