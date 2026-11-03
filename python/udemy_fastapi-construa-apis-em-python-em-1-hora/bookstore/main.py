from fastapi import FastAPI
from fastapi.exceptions import HTTPException
import random
from typing import Dict, List
import os
import json


app = FastAPI()

# /                             -> boas vidnas
# /list-books                   -> listar todos os livros
# /list-book-by-index/{index}   -> listar um livro
# /get-random-book              -> livro aleatório
# /add-book                     -> adicionar novo livro



"""
List and Add from json file 
"""

BOOK_DATABASE2 = [] 

BOOKS_FILE = "books.json"

if os.path.exists(BOOKS_FILE):
    with open(BOOKS_FILE, "r") as f:
        BOOK_DATABASE2 = json.load(f)


# /list-books2 
@app.get("/list-books2")
async def list_books2():
    return {"books": BOOK_DATABASE2}


# /add-book2    -> add new bokk to json file 
@app.post("/add-book2")
async def add_book2(book: str):
    BOOK_DATABASE2.append(book)
    with open (BOOKS_FILE, "w") as f:
        json.dump(BOOK_DATABASE2, f)
    return { "message": f"The book {book} was added"}



"""
First example: list and add in memory
"""
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


# /add-book                     -> adicionar novo livro
@app.post("/add-book")
async def add_book(book: str):
    BOOK_DATABASE.append(book)
    return { "message": f"Book {book} was added"}




"""
Some tests using type 
"""
# /check -> route created to do some tests 
@app.get("/check")
async def check():
    result = { "books": BOOK_DATABASE}
    print(type(result))
    return result

# /check2 -> route created to try dict definition
@app.get("/check2")
async def check2() -> dict:
    return { "book": BOOK_DATABASE }

# /check3 -> route created to try Dict[str, List[str]] method to specify the type of dict and list type 
# need to import Dict and List as the command "from typing import Dict, List"
@app.get("/check3")
async def check3() -> Dict[str, List[str]]:
    return { "book": BOOK_DATABASE }
