from db_connection import get_connection
#----------------Manage books------------------
#add books-----------
class add_book:
     def __init__(self, book_id,title,author,isbn,section,stock_count,status):
         conn = get_connection() 
         cursor = conn.cursor() 
    
         cursor.execute("USE lms")
  
         cursor.execute( 
             "INSERT INTO books(book_id,title,author,isbn,section,stock_count,status)\
             VALUES (%s, %s, %s, %s, %s, %s, %s)", 
             (book_id,title,author,isbn,section,stock_count,status ) 
         ) 
  
         conn.commit() 
         cursor.close() 
         conn.close() 
         print(f"Added book: {title}")

# ---------- READ (all) ---------- 

def get_all_books():
    conn = get_connection() 
    cursor = conn.cursor() 
    
    cursor.execute("USE lms")
    
    cursor.execute("SELECT * FROM books") 
    rows = cursor.fetchall()
   
    cursor.close() 
    conn.close() 
    return rows         
# ---------- READ (one) ---------- 

def get_one_book():
    conn = get_connection() 
    cursor = conn.cursor() 
    
    cursor.execute("USE lms")
    
    cursor.execute("SELECT * FROM books") 
    rows = cursor.fetchone()
   
    cursor.close() 
    conn.close() 
    return rows         

# ---------- UPDATE ----------
def update_stock(book_id, new_stock): 
    conn = get_connection() 
    cursor = conn.cursor() 
    
    cursor.execute("USE lms")
  
    cursor.execute( 
        "UPDATE books SET stock_count = %s WHERE id = %s", 
        (new_salary, employee_id) 
    ) 
  
    conn.commit() 
    cursor.close() 
    conn.close() 
    print(f"Updated book stock {book_id}'s stock to {new_stock}") 


# ---------- DELETE ---------- 
def delete_book(book_id): 
    conn = get_connection() 
    cursor = conn.cursor() 
  
    cursor.execute("USE lms")
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,)) 
  
    conn.commit() 
    cursor.close() 
    conn.close() 
    print(f"Deleted book {book_id}") 