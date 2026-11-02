from fastapi import FastAPI

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
