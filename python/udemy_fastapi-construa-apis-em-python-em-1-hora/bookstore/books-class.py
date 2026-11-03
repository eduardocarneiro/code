import json 
import os
from fastapi import FastAPI, HTTPException
import random
from pydantic import BaseModel
from uuid import uuid4 
from typing import Literal, Optional
from fastapi.encoders import jsonable_encoder

app = FastAPI()

class Book (BaseModel):
    name: str
    price: float
    book_id: Optional[str] = uuid4().hex 
    genre: Literal["fiction", "non-fiction"]


BOOKS = []
BOOKS_FILE = "books-class.json"

# Open the json file as readonly
if os.path.exists(BOOKS_FILE):
    with open (BOOKS_FILE, "r") as f:
        BOOKS = json.load(BOOKS_FILE)


# /list-books       -> route to list all books
@app.get("/list-books")
async def list_books():
    return { "Books": BOOKS}


# /add-books        -> route to add a new book 
@app.post("/add-books")
async def add_books(book: Book):
    json_book = jsonable_encoder(book)

    book.book_id = uuid4().hex
    BOOKS.append(json_book)
    with open (BOOKS_FILE, "w") as f:
        json.dump(BOOKS, f)
    return { "message": f"Book '{book}' was added!"}

