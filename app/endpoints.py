from fastapi import APIRouter
from app.database import get_films

# Initilize router
router = APIRouter()

# /ping
@router.get("/ping")
def ping():
    return {"status": "ok"}

# /getFilms
@router.get("/getFilms")
def get_films_endpoint():
    return get_films()

# /getFilmData
from fastapi import HTTPException
from app.database import get_film_data

@router.get("/getFilmData")
def get_film_data_endpoint(id: int):
    film = get_film_data(id)

    if film is None:
        raise HTTPException(status_code=404,detail="ID not found")

    return film
