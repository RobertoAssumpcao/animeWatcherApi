from pydantic import BaseModel
from datetime import datetime
from typing import List
from Models.anime import Anime

class AnimeSchemaRequest(BaseModel):
    """
    DTO para criação de novo anime
    """
    titulo: str = "Nome do anime"
    genero: str = "Gênero"
    episodios: int = 0
    status: str = "Assistido"

class AnimeSchemaResponse(BaseModel):
    """
    DTO de resposta com os dados de um anime
    """
    id: int = 0
    titulo: str = "Nome do anime"
    genero: str = "Gênero"
    episodios: int = 0
    status: str = "Assistido"
    data_insercao: datetime = None

class AnimeListSchemaResponse(BaseModel):
    """
    DTO para lista de animes
    """
    animes: List[AnimeSchemaResponse]

class AnimeSchemaRemove(BaseModel):
    """
    DTO para remoção de anime
    """
    id: int = 0

def list_animes(animes: list[Anime]):
    result = []

    for item in animes:
        result.append({
            "id": item.id,
            "titulo": item.titulo,
            "genero": item.genero,
            "episodios": item.episodios,
            "status": item.status,
            "data_insercao": item.data_insercao
        })

    return {"animes": result}
