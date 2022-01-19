from dataclasses import dataclass

@dataclass
class Filme:
    titulo: str
    sinopse: str
    tempoDuracao: int
    avaliacao: int

@dataclass
class Serie:
    titulo: str
    sinopse: str
    tempoDuracao: int
    qtdEpisodio: int
    avaliacao: int

@dataclass
class Documento:
    filme: Filme
    serie: Serie