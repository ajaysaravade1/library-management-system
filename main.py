from fastapi import FastAPI, HTTPException
import models

app = FastAPI()

# Member Endpoints

@app.post("/lms/members/")
def create_member(member_data: dict):
    return models.create_member(member_data)

@app.get("/lms/members/{id}")
def get_member(id: str):
    member = models.get_member(id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member

@app.put("/lms/members/{id}")
def update_member(id: str, update_data: dict):
    return models.update_member(id, update_data)

@app.delete("/lms/members/{id}")
def delete_member(id: str):
    return models.delete_member(id)

@app.get("/lms/members")
def get_all_members():
    return models.get_all_members()

@app.get("/lms/membershistory")
def get_members_history():
    return models.get_member_history()

@app.get("/lms/active_members")
def get_active_members():
    return models.get_active_members()

@app.get("/lms/deleted_members")
def get_deleted_members():
    return models.get_deleted_members()

# Book Endpoints

@app.post("/lms/books")
def create_book(book_data: dict):
    return models.create_book(book_data)

@app.get("/lms/books/{id}")
def get_book(id: str):
    book = models.get_book(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/lms/books/{id}")
def update_book(id: str, book_data: dict):
    return models.update_book(id, book_data)

@app.delete("/lms/books/{id}")
def delete_book(id: str):
    return models.delete_book(id)
