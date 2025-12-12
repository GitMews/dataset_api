from fastapi import APIRouter, HTTPException, Depends
from app.database import get_films, get_film_data
from app.security import check_api_key

# Initilize router
router = APIRouter()

# /ping
@router.get("/ping")
def ping():
    return {"status": "ok"}

# /getFilms
@router.get("/getFilms", dependencies=[Depends(check_api_key)])
def get_films_endpoint():
    return get_films()

# /getFilmData
@router.get("/getFilmData", dependencies=[Depends(check_api_key)])
def get_film_data_endpoint(id: int):
    film = get_film_data(id)

    if film is None:
        raise HTTPException(status_code=404,detail="ID not found")

    return film
