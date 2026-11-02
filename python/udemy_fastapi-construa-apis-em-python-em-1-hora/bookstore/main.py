from logging import raiseExceptions

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
import random


app = FastAPI()

# /                             -> boas vidnas
# /list-books                   -> listar todos os livros
# /list-book-by-index/{index}   -> listar um livro
# /get-random-book              -> livro aleatório
# /add-book                     -> adicionar novo livro


BOOK_DATABASE = [
    "Harry Potter",
    "Lord of the rings",
    "the da vinci code"
]

###
# / 
@app.get("/")
async def root():
    return "welcome to my bookstore"


# /list-books 
@app.get("/list-books")
async def list_books():
    return {"books": BOOK_DATABASE}


# /list-book-by-index/{index}
@app.get("/list-book-by-index/{index}")
async def list_book_by_index(index: int):
    if index < 0 or index >= len(BOOK_DATABASE):
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
        raise HTTPException(404, 'Index out of range')
    else:
        return { "books": BOOK_DATABASE[index] }


# /get-random-book              -> livro aleatório
@app.get("/get-random-book")
async def get_random_book():
    return random.choice(BOOK_DATABASE)


