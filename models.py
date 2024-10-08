import database

# Member model queries

def create_member(member_data):
    cursor = database.get_cursor()
    try:
        query = """INSERT INTO Members (id, username, passwd, m_name, email, membership_date)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (
            member_data['id'], 
            member_data['username'], 
            member_data['passwd'], 
            member_data['m_name'], 
            member_data['email'], 
            member_data['membership_date']
        ))
        database.connection.commit()
        return {"message": "Member created successfully"}
    except Exception as e:
        database.connection.rollback()
        raise e

def get_member(member_id):
    cursor = database.get_cursor()
    query = "SELECT * FROM Members WHERE id = %s"
    cursor.execute(query, (member_id,))
    return cursor.fetchone()

def update_member(member_id, update_data):
    cursor = database.get_cursor()
    query = """UPDATE Members SET username=%s, passwd=%s, m_name=%s, email=%s, membership_date=%s
               WHERE id=%s"""
    cursor.execute(query, (
        update_data['username'], 
        update_data['passwd'], 
        update_data['m_name'], 
        update_data['email'], 
        update_data['membership_date'], 
        member_id
    ))
    database.connection.commit()
    return {"message": "Member updated successfully"}

def delete_member(member_id):
    cursor = database.get_cursor()
    query = "DELETE FROM Members WHERE id = %s"
    cursor.execute(query, (member_id,))
    database.connection.commit()
    return {"message": "Member deleted successfully"}

def get_all_members():
    cursor = database.get_cursor()
    query = "SELECT * FROM Members"
    cursor.execute(query)
    return cursor.fetchall()

def get_member_history():
    cursor = database.get_cursor()
    query = "SELECT * FROM Members UNION SELECT * FROM Deleted_Members"
    cursor.execute(query)
    return cursor.fetchall()

def get_active_members():
    cursor = database.get_cursor()
    query = "SELECT * FROM Members"
    cursor.execute(query)
    return cursor.fetchall()

def get_deleted_members():
    cursor = database.get_cursor()
    query = "SELECT * FROM Deleted_Members"
    cursor.execute(query)
    return cursor.fetchall()

# Book model queries (similar to members)

def create_book(book_data):
    cursor = database.get_cursor()
    query = """INSERT INTO Books (id, title, authour, isbn, publish_year, stat)
               VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (
        book_data['id'], 
        book_data['title'], 
        book_data['authour'], 
        book_data['isbn'], 
        book_data['publish_year'], 
        book_data['stat']
    ))
    database.connection.commit()
    return {"message": "Book created successfully"}

def get_all_books():
    cursor = database.get_cursor()
    query = "SELECT * FROM Books"
    cursor.execute(query)
    return cursor.fetchall()


def get_book(book_id):
    cursor = database.get_cursor()
    query = "SELECT * FROM Books WHERE id = %s"
    cursor.execute(query, (book_id,))
    return cursor.fetchone()

def update_book(book_id, book_data):
    cursor = database.get_cursor()
    query = """UPDATE Books SET title=%s, authour=%s, isbn=%s, publish_year=%s, stat=%s
               WHERE id=%s"""
    cursor.execute(query, (
        book_data['title'], 
        book_data['authour'], 
        book_data['isbn'], 
        book_data['publish_year'], 
        book_data['stat'], 
        book_id
    ))
    database.connection.commit()
    return {"message": "Book updated successfully"}

def delete_book(book_id):
    cursor = database.get_cursor()
    query = "DELETE FROM Books WHERE id = %s"
    cursor.execute(query, (book_id,))
    database.connection.commit()
    return {"message": "Book deleted successfully"}


def get_member_books():
    cursor = database.get_member_cursor()
    query = "SELECT * FROM Books"
    cursor.execute(query)    
    return cursor.fetchall() 

def borrow(borrow_data):
    cursor = database.get_member_cursor()
    query = """INSERT INTO Borrow (id, book_id, member_id, borrow_date, return_date)
               VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(query, (
        borrow_data['id'], 
        borrow_data['book_id'], 
        borrow_data['member_id'], 
        borrow_data['borrow_date'], 
        borrow_data['return_date']    
    ))
    database.connection.commit()
    return {"message": "Borrow entry created successfully"}

def return_book(id):
    cursor = database.get_member_cursor()
    query = """UPDATE Borrow SET return_date = NOW() WHERE id = %s"""
    cursor.execute(query,(id))
    database.connection.commit()
    return {"message": "Book returned successfully"}

def delete_member(id):
    cursor = database.get_member_cursor()
    query = "DELETE FROM Members WHERE id = %s"
    cursor.execute(query, (id,))
    database.connection.commit()
    return {"message": "Memeber deleted successfully"}


def view_member_book_history(id):
    cursor = database.get_member_cursor()
    query = "SELECT * FROM Borrow WHERE member_id = %s"
    cursor.execute(query)    
    return cursor.fetchall() 