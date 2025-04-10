from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from Models import Session, Anime
from sqlalchemy.exc import IntegrityError
from schemas.errorSchema import ErrorSchema
from schemas.animeSchema import AnimeSchemaRemove, AnimeListSchemaResponse, AnimeSchemaRequest, list_animes

info = Info(title="Health care", version="1.0.0")
app = OpenAPI(__name__, info = info)
CORS(app)

swagger_tag = Tag(name="Swagger", description="Swagger endpoints")
Anime_tag = Tag(name="Anime", description="Anime endpoints")

@app.get('/', tags=[swagger_tag])
def home():
    """
    A rota padrão leva você às opções de documentação do endpoint.
    """
    return redirect('/openapi')

@app.post('/Anime', tags=[Anime_tag], 
          responses =
          {
              "200": AnimeListSchemaResponse, "400": ErrorSchema, "409": ErrorSchema, "500": ErrorSchema
          })
def add_Anime(form: AnimeSchemaRequest):
    """
    endpoint usado para adicionar uma nova Anime e retorna a lista das que já foram registradas.
    """

    Anime = Anime(
        nome= form.nome,
        Anime= form.Anime
    )

    try:
        session = Session()
        session.add(Anime)
        session.commit()

        Animes = session.query(Anime).all()

        session.close()

        if not Animes:
            return {"message": "Glucoses not found"}, 404
        else:
            return list_animes(Animes), 200
    except IntegrityError as ex:
        {"message": "Anime já registrada no banco de dados"}, 409
    except Exception as ex:
        {"message": "não foi possível salvar"}, 500
    

@app.get('/Animes', tags=[Anime_tag], 
         responses = 
         {
             "200": AnimeListSchemaResponse, "404": ErrorSchema, "500": ErrorSchema
         })
def get_all_Animes():
    """
    endpoint usado para listar todas as Animes registradas.
    """
    try:
        session = Session()
        Animes = session.query(Anime).all()
        
        session.close()

        if not Animes:
            return {"message": "Glucoses not found"}, 404
        else:
            return list_animes(Animes), 200
    except Exception as ex:
        return {"message": ex}, 500

@app.delete('/Anime', tags=[Anime_tag],
            responses={"200": AnimeListSchemaResponse, "404": ErrorSchema, "500": ErrorSchema})
def del_Anime(query: AnimeSchemaRemove):
    """Deleta um registro de Anime
    Retorna uma lista de Animes.
    """

    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Anime).filter(Anime.id == query.id).delete()
    session.commit()

    Animes = session.query(Anime).all()

    session.close()

    try:
        if count:
            return list_animes(Animes), 200
        else:
            return {"mesage": "Anime não encontrado."}, 404
    except Exception as ex:
        return {"message": ex}, 500