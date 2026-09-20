from db_connection import get_connection
#-------------manage transactin-----------
#-----create
class add_transaction:
     def __init__(self,trasaction_id,book_id,member_id,librarian_id,issue_date,return_date):
         conn = get_connection() 
         cursor = conn.cursor() 
    
         cursor.execute("USE lms")
  
         cursor.execute( 
             "INSERT INTO members(trasaction_id,book_id,member_id,librarian_id,issue_date,return_date)\
             VALUES (%s, %s, %s, %s, %s, %s)", 
             (trasaction_id,book_id,member_id,librarian_id,issue_date,return_date) 
         ) 
  
         conn.commit() 
         cursor.close() 
         conn.close() 
         print(f"transaction completed: {trasaction_id}")

# ---------- READ (all) ---------- 

def get_all_trasactions():
    conn = get_connection() 
    cursor = conn.cursor() 
    
    cursor.execute("USE lms")
    
    cursor.execute("SELECT * FROM transaction") 
    rows = cursor.fetchall()
   
    cursor.close() 
    conn.close() 
    return rows
# ---------- READ (one) ---------- 

def get_one_trasactions():
    conn = get_connection() 
    cursor = conn.cursor() 
    
    cursor.execute("USE lms")
    
    cursor.execute("SELECT * FROM transaction") 
    rows = cursor.fetchone()
   
    cursor.close() 
    conn.close() 
    return rows

# ---------- UPDATE ----------
def update_book(transaction_id, new_book): 
    conn = get_connection() 
    cursor = conn.cursor() 
    
    cursor.execute("USE lms")
  
    cursor.execute( 
        "UPDATE transactions SET book = %s WHERE id = %s", 
        (new_book, transaction_id) 
    ) 
    conn.commit() 
    cursor.close() 
    conn.close() 
    print(f"Updated book {transaction_id}'s email to {new_book}") 

# ---------- DELETE ---------- 
def delete_transaction(transaction_id): 
    conn = get_connection() 
    cursor = conn.cursor() 
  
    cursor.execute("USE lms")
    cursor.execute("DELETE FROM transactions WHERE id = %s", (transaction_id,)) 
  
    conn.commit() 
    cursor.close() 
    conn.close() 
    print(f"Deleted transaction{transaction_id}") 