from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from Models import Session, Anime
from sqlalchemy.exc import IntegrityError
from schemas.errorSchema import ErrorSchema
from schemas.animeSchema import (
    AnimeSchemaRemove,
    AnimeListSchemaResponse,
    AnimeSchemaRequest,
    AnimeSchemaPath,
    list_animes
)

info = Info(title="Anime Watcher API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

swagger_tag = Tag(name="Swagger", description="Swagger endpoints")
anime_tag = Tag(name="Anime", description="Gerenciamento de animes assistidos")

@app.get('/', tags=[swagger_tag])
def home():
    """
    Redireciona para a documentação interativa da API.
    """
    return redirect('/openapi')


@app.post('/anime', tags=[anime_tag],
          responses={
              "200": AnimeListSchemaResponse,
              "400": ErrorSchema,
              "409": ErrorSchema,
              "500": ErrorSchema
          })
def add_anime(form: AnimeSchemaRequest):
    """
    Adiciona um novo anime e retorna a lista atualizada de animes.
    """
    anime = Anime(
        titulo=form.titulo,
        genero=form.genero,
        episodios=form.episodios,
        status=form.status
    )

    try:
        session = Session()
        session.add(anime)
        session.commit()

        animes = session.query(Anime).all()
        session.close()

        return list_animes(animes), 200

    except IntegrityError:
        return {"message": "Anime já registrado no banco de dados"}, 409
    except Exception:
        return {"message": "Não foi possível salvar o anime"}, 500


@app.get('/animes', tags=[anime_tag],
         responses={
             "200": AnimeListSchemaResponse,
             "404": ErrorSchema,
             "500": ErrorSchema
         })
def get_all_animes():
    """
    Lista todos os animes registrados.
    """
    try:
        session = Session()
        animes = session.query(Anime).all()
        session.close()

        if not animes:
            return {"message": "Nenhum anime encontrado"}, 404
        else:
            return list_animes(animes), 200
    except Exception as ex:
        return {"message": str(ex)}, 500


@app.delete('/anime', tags=[anime_tag],
            responses={
                "200": AnimeListSchemaResponse,
                "404": ErrorSchema,
                "500": ErrorSchema
            })
def delete_anime(query: AnimeSchemaRemove):
    """
    Remove um anime pelo ID e retorna a lista atualizada.
    """
    session = Session()
    count = session.query(Anime).filter(Anime.id == query.id).delete()
    session.commit()

    animes = session.query(Anime).all()
    session.close()

    try:
        if count:
            return list_animes(animes), 200
        else:
            return {"message": "Anime não encontrado"}, 404
    except Exception as ex:
        return {"message": str(ex)}, 500


@app.put('/anime/<int:id>', tags=[anime_tag],
         responses={
             "200": AnimeListSchemaResponse,
             "404": ErrorSchema,
             "400": ErrorSchema,
             "500": ErrorSchema
         })
def update_anime(path: AnimeSchemaPath, form: AnimeSchemaRequest):
    """
    Atualiza um anime existente pelo ID.
    """
    try:
        session = Session()
        anime = session.query(Anime).filter(Anime.id == path.id).first()

        if not anime:
            session.close()
            return {"message": "Anime não encontrado"}, 404

        anime.titulo = form.titulo
        anime.genero = form.genero
        anime.episodios = form.episodios
        anime.status = form.status

        session.commit()
        animes = session.query(Anime).all()
        session.close()

        return list_animes(animes), 200

    except Exception as ex:
        return {"message": f"Erro ao atualizar: {str(ex)}"}, 500
