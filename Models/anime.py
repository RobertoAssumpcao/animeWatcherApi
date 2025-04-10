from sqlalchemy import Column, String, Integer, DateTime, UniqueConstraint
from datetime import datetime
from typing import Union

from Models import Base

class Anime(Base):
    __tablename__ = 'anime_catalog'

    id = Column("pk_anime", Integer, primary_key=True)

    titulo = Column(String(140))
    genero = Column(String(100))
    episodios = Column(Integer)
    status = Column(String(100))  # Ex: Assistido, Assistindo, Planejo Ver
    data_insercao = Column(DateTime, default=datetime.now())

    __table_args__ = (UniqueConstraint("titulo", "status", name="anime_unique_id"),)

    def __init__(self, titulo, genero, episodios, status,
                 data_insercao: Union[DateTime, None] = None):
        """
        Cria um Anime

        Arguments:
            titulo: título do anime
            genero: gênero do anime
            episodios: número de episódios
            status: status de visualização (Assistido, Assistindo, etc.)
            data_insercao: data de quando o anime foi inserido no sistema
        """
        self.titulo = titulo
        self.genero = genero
        self.episodios = episodios
        self.status = status

        if data_insercao:
            self.data_insercao = data_insercao

    def to_dict(self):
        """
        Retorna a representação em dicionário do Anime.
        """
        return {
            "id": self.id,
            "titulo": self.titulo,
            "genero": self.genero,
            "episodios": self.episodios,
            "status": self.status,
            "data_insercao": self.data_insercao
        }

    def __repr__(self):
        return f"Anime(id={self.id}, titulo='{self.titulo}', genero='{self.genero}', episodios={self.episodios}, status='{self.status}')"
